from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import base64
import schedule
import time
import threading
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time_capsule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

db = SQLAlchemy(app)
CORS(app)

# Configurações de email (configure com seus dados)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'seu_email@gmail.com',
    'password': 'sua_senha_app'  # Use senha de app para Gmail
}

# Criar diretório de uploads se não existir
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Modelo da Cápsula do Tempo
class TimeCapsule(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    image_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sent = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'delivery_date': self.delivery_date.isoformat(),
            'created_at': self.created_at.isoformat(),
            'sent': self.sent,
            'has_image': bool(self.image_path)
        }

# Criar tabelas
with app.app_context():
    db.create_all()

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/capsule', methods=['POST'])
def create_capsule():
    try:
        data = request.form
        
        # Validar dados obrigatórios
        if not all(key in data for key in ['name', 'email', 'message', 'delivery_date']):
            return jsonify({'error': 'Campos obrigatórios: name, email, message, delivery_date'}), 400
        
        # Validar formato da data
        try:
            delivery_date = datetime.strptime(data['delivery_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Formato de data inválido. Use YYYY-MM-DD'}), 400
        
        # Verificar se a data é no futuro
        if delivery_date <= date.today():
            return jsonify({'error': 'A data de entrega deve ser no futuro'}), 400
        
        # Processar imagem se fornecida
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                image_path = file_path
        
        # Criar nova cápsula
        capsule = TimeCapsule(
            name=data['name'],
            email=data['email'],
            message=data['message'],
            delivery_date=delivery_date,
            image_path=image_path
        )
        
        db.session.add(capsule)
        db.session.commit()
        
        return jsonify({
            'message': 'Cápsula do tempo criada com sucesso!',
            'capsule_id': capsule.id,
            'delivery_date': delivery_date.isoformat()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/capsules', methods=['GET'])
def get_capsules():
    """Endpoint para listar cápsulas (para admin/debug)"""
    try:
        capsules = TimeCapsule.query.all()
        return jsonify([capsule.to_dict() for capsule in capsules])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/capsule/<capsule_id>', methods=['GET'])
def get_capsule(capsule_id):
    """Endpoint para obter uma cápsula específica"""
    try:
        capsule = TimeCapsule.query.get_or_404(capsule_id)
        return jsonify(capsule.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def send_email(capsule):
    """Função para enviar email da cápsula"""
    try:
        # Configurar servidor SMTP
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
        
        # Criar mensagem
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['email']
        msg['To'] = capsule.email
        msg['Subject'] = f'🕰️ Sua Cápsula do Tempo chegou, {capsule.name}!'
        
        # Corpo do email
        body = f"""
        Olá {capsule.name}!
        
        Sua cápsula do tempo finalmente chegou! 🎉
        
        Você escreveu esta mensagem em {capsule.created_at.strftime('%d/%m/%Y')} para ser entregue hoje ({capsule.delivery_date.strftime('%d/%m/%Y')}).
        
        Aqui está sua mensagem do passado:
        
        "{capsule.message}"
        
        Esperamos que esta mensagem traga boas lembranças e reflexões!
        
        Com carinho,
        Cápsula do Tempo Virtual
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Anexar imagem se existir
        if capsule.image_path and os.path.exists(capsule.image_path):
            with open(capsule.image_path, 'rb') as f:
                img_data = f.read()
                image = MIMEImage(img_data)
                image.add_header('Content-Disposition', 'attachment', filename='imagem_capsula.jpg')
                msg.attach(image)
        
        # Enviar email
        server.send_message(msg)
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False

def check_and_send_capsules():
    """Função para verificar e enviar cápsulas pendentes"""
    try:
        with app.app_context():
            today = date.today()
            pending_capsules = TimeCapsule.query.filter(
                TimeCapsule.delivery_date <= today,
                TimeCapsule.sent == False
            ).all()
            
            for capsule in pending_capsules:
                print(f"Enviando cápsula para {capsule.email}...")
                
                if send_email(capsule):
                    capsule.sent = True
                    db.session.commit()
                    print(f"Cápsula enviada com sucesso para {capsule.email}")
                else:
                    print(f"Falha ao enviar cápsula para {capsule.email}")
                    
    except Exception as e:
        print(f"Erro ao verificar cápsulas: {e}")

def schedule_checker():
    """Função para executar o agendador"""
    schedule.every().day.at("09:00").do(check_and_send_capsules)
    schedule.every().day.at("18:00").do(check_and_send_capsules)  # Verificar 2x por dia
    
    while True:
        schedule.run_pending()
        time.sleep(3600)  # Verificar a cada hora

@app.route('/api/test-email', methods=['POST'])
def test_email():
    """Endpoint para testar envio de email"""
    try:
        data = request.json
        email = data.get('email')
        
        if not email:
            return jsonify({'error': 'Email é obrigatório'}), 400
        
        # Criar cápsula de teste
        test_capsule = TimeCapsule(
            name="Teste",
            email=email,
            message="Esta é uma mensagem de teste da sua cápsula do tempo virtual!",
            delivery_date=date.today()
        )
        
        if send_email(test_capsule):
            return jsonify({'message': 'Email de teste enviado com sucesso!'})
        else:
            return jsonify({'error': 'Falha ao enviar email de teste'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/force-check', methods=['POST'])
def force_check():
    """Endpoint para forçar verificação de cápsulas (para debug)"""
    try:
        check_and_send_capsules()
        return jsonify({'message': 'Verificação de cápsulas executada'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Iniciar thread do agendador
    scheduler_thread = threading.Thread(target=schedule_checker, daemon=True)
    scheduler_thread.start()
    
    print("🕰️ Cápsula do Tempo Virtual iniciada!")
    print("📧 Verificações de email agendadas para 09:00 e 18:00 diariamente")
    print("🚀 API rodando na porta 5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)