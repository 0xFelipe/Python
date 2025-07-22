
# 🕰️ Cápsula do Tempo Virtual

Este projeto foi criado como um **auto-desafio** inspirado no vídeo da Codecon:  
📺 [1 Sênior vs. 1 Júnior (mas com IA) - Codecon](https://youtu.be/ad046g56LZk)

## 💡 Desafio
A proposta era: **Será que eu conseguiria fazer uma API funcional de cápsula do tempo em 1 hora?**
A resposta foi: **sim!** Finalizei o projeto em menos de uma hora e coloquei para rodar localmente utilizando:
- XAMPP
- Abertura de portas lógicas
- No-IP para tornar o IP externo amigável

## 🔧 Tecnologias Utilizadas

### Backend (API)
- Python 3
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- SQLite
- Agendamento com `schedule`
- Envio de e-mail com `smtplib`
- Upload de imagem com limite de 16MB
- Threads para execução contínua

### Frontend
- HTML5 / CSS3 responsivo
- Javascript puro (sem dependências externas)
- Formulário interativo com preview de imagem
- Contador de caracteres dinâmico
- Placeholder animado com dicas de escrita

## ✉️ Como Funciona

1. Você preenche um formulário com:
   - Nome
   - E-mail
   - Mensagem para o futuro
   - Data de entrega (obrigatoriamente no futuro)
   - (Opcional) Imagem

2. Sua cápsula é armazenada no banco local e programada para ser entregue na data definida.
3. O sistema verifica automaticamente 2 vezes ao dia se há cápsulas para enviar.
4. No dia da entrega, você recebe a mensagem por e-mail — junto com a imagem, se fornecida.

## 📦 Arquivos Incluídos

- `time_capsule_backend.py` → Backend completo com API, banco, agendador e envio de e-mails.
- `time_capsule_frontend.html` → Interface simples e bonita para preencher sua cápsula.

## 🛠️ Como Rodar Localmente

1. Instale as dependências com `pip install flask flask_sqlalchemy flask_cors schedule`
2. Configure as variáveis de e-mail no dicionário `EMAIL_CONFIG` no backend.
3. Execute o backend com `python time_capsule_backend.py`
4. Abra o `time_capsule_frontend.html` no navegador e teste

## 🔐 Observações

- Recomenda-se utilizar uma senha de aplicativo para o Gmail.
- Ideal para rodar em uma VM, Raspberry Pi ou servidor com IP fixo.

## 🚀 Resultado

> Projeto finalizado em tempo recorde, funcional e com potencial de expansão.

Se quiser testar e contribuir, fique à vontade! Feedbacks são bem-vindos! 😊

---
**Feito com dedicação e curiosidade por Felipe.**
