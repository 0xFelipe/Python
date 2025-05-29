import json
import re
import requests
import os
from dotenv import load_dotenv
from xml.etree import ElementTree as ET
import time
from randomcolor import RandomColor


# Carrega variáveis do arquivo .env
load_dotenv()

class KMLToAPIConverter:
    def __init__(self):
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.api_url = os.getenv("API_URL")
        
        if not self.bearer_token:
            raise ValueError("BEARER_TOKEN não encontrado no arquivo .env")
        if not self.api_url:
            raise ValueError("API_URL não encontrado no arquivo .env")
    
    def extrair_placemarks_do_kml(self, caminho_arquivo):
        """
        Extrai placemarks do arquivo KML
        
        Args:
            caminho_arquivo (str): Caminho para o arquivo KML
            
        Returns:
            list: Lista de dicionários com name e coordinates
        """
        try:
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()
            
            # Remove namespace do KML se existir
            if root.tag.startswith('{'):
                namespace = root.tag.split('}')[0] + '}'
            else:
                namespace = ''
            
            placemarks = []
            
            # Busca todos os elementos Placemark
            for placemark in root.iter(f'{namespace}Placemark'):
                name_element = placemark.find(f'{namespace}name')
                coordinates_element = placemark.find(f'.//{namespace}coordinates')
                
                if name_element is not None and coordinates_element is not None:
                    name = name_element.text.strip() if name_element.text else "Zona sem nome"
                    coordinates = coordinates_element.text.strip() if coordinates_element.text else ""
                    
                    if coordinates:
                        placemarks.append({
                            'name': name,
                            'coordinates': coordinates
                        })
            
            print(f"Encontrados {len(placemarks)} placemarks no arquivo KML")
            return placemarks
            
        except ET.ParseError as e:
            print(f"Erro ao fazer parse do XML: {e}")
            return []
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho_arquivo}")
            return []
        except Exception as e:
            print(f"Erro inesperado ao processar KML: {e}")
            return []
    
    def processar_coordenadas(self, coordinates_text):
        """
        Processa string de coordenadas e converte para array
        
        Args:
            coordinates_text (str): Texto com coordenadas
            
        Returns:
            list: Array de coordenadas [lng, lat]
        """
        # Remove quebras de linha e espaços extras
        coordinates_text = coordinates_text.strip()
        
        # Divide as coordenadas (podem estar separadas por espaços ou quebras de linha)
        coordenadas_raw = re.split(r'\s+', coordinates_text)
        coordenadas_array = []
        
        for coord in coordenadas_raw:
            coord = coord.strip()
            if coord:  # Ignora strings vazias
                # Divide por vírgula e pega apenas lng, lat (ignora Z se existir)
                partes = coord.split(',')
                if len(partes) >= 2:
                    try:
                        lng = float(partes[0])
                        lat = float(partes[1])
                        coordenadas_array.append([lng, lat])
                    except ValueError:
                        print(f"Coordenada inválida ignorada: {coord}")
                        continue
        
        # Verifica se o polígono está fechado (primeira == última coordenada)
        if coordenadas_array and len(coordenadas_array) > 2:
            if coordenadas_array[0] != coordenadas_array[-1]:
                coordenadas_array.append(coordenadas_array[0])  # Fecha o polígono
        
        return coordenadas_array
    
    def criar_objeto(self, name, coordinates_array, zone_id=None):
        rand_color = RandomColor()
        hex_color = rand_color.generate(luminosity="bright")[0] 
        """
        Cria objeto no formato 
        
        Args:
            name (str): Nome da zona
            coordinates_array (list): Array de coordenadas
            zone_id (int): ID da zona
            
        Returns:
            dict: Objeto no formato 
        """
        # Gera ID automático se não fornecido
        if zone_id is None:
            zone_id = abs(hash(str(coordinates_array) + name)) % 100000
        
        return {
            "id": zone_id,
            "name": name,
            "order": 0,
            "layer_type": "polygon",
            "coordinates": {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coordinates_array]
                },
                "properties": []
            },
            "fill_color": hex_color
        }
    
    def enviar_para(self, zona_data):
        """
        Envia dados da zona para API 
        
        Args:
            zona_data (dict): Dados da zona no formato 
            
        Returns:
            bool: True se sucesso, False se falha
        """
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=zona_data,
                timeout=30
            )
            
            if response.status_code in [200, 201]:
                print(f"✅ Zona '{zona_data['name']}' enviada com sucesso (ID: {zona_data['id']})")
                return True
            else:
                print(f"❌ Erro ao enviar zona '{zona_data['name']}': {response.status_code}")
                print(f"   Resposta: {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão ao enviar zona '{zona_data['name']}': {e}")
            return False
    
    def processar_arquivo_kml(self, caminho_arquivo, delay_entre_requisicoes=1):
        """
        Processa arquivo KML completo e envia todas as zonas para 
        
        Args:
            caminho_arquivo (str): Caminho para o arquivo KML
            delay_entre_requisicoes (int): Delay em segundos entre requisições
        """
        print(f"Processando arquivo KML: {caminho_arquivo}")
        print("="*60)
        
        # Extrai placemarks do KML
        placemarks = self.extrair_placemarks_do_kml(caminho_arquivo)
        
        if not placemarks:
            print("Nenhum placemark válido encontrado no arquivo KML")
            return
        
        sucessos = 0
        falhas = 0
        
        for i, placemark in enumerate(placemarks, 1):
            print(f"\nProcessando zona {i}/{len(placemarks)}: {placemark['name']}")
            
            # Processa coordenadas
            coordinates_array = self.processar_coordenadas(placemark['coordinates'])
            
            if len(coordinates_array) < 3:
                print(f"⚠️  Zona '{placemark['name']}' possui coordenadas insuficientes - ignorada")
                falhas += 1
                continue
            
            # Cria objeto 
            zona_data = self.criar_objeto(placemark['name'], coordinates_array)
            
            # Envia para API
            if self.enviar_para(zona_data):
                sucessos += 1
            else:
                falhas += 1
            
            # Delay entre requisições para não sobrecarregar a API
            if i < len(placemarks) and delay_entre_requisicoes > 0:
                time.sleep(delay_entre_requisicoes)
        
        print("\n" + "="*60)
        print(f"RESUMO: {sucessos} zonas enviadas com sucesso, {falhas} falhas")
        print("="*60)

def criar_arquivo_env_exemplo():
    """Cria arquivo .env de exemplo se não existir"""
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("""# Token Bearer para autenticação na API 
BEARER_TOKEN=seu_token_aqui
API_URL=""# URL da API para onde os dados serão enviados                    

""")
        print("Arquivo .env criado. Por favor, configure o BEARER_TOKEN")
        print("Arquivo .env criado. Por favor, configure o API_URL")
        return False
    return True

def main():
    print("=== CONVERSOR KML PARA  API ===\n")
    
    # Verifica se arquivo .env existe
    if not criar_arquivo_env_exemplo():
        return
    
    try:
        converter = KMLToAPIConverter()
    except ValueError as e:
        print(f"Erro de configuração: {e}")
        print("Por favor, configure o arquivo .env corretamente")
        return
    
    # Solicita caminho do arquivo KML
    caminho_kml = input("Digite o caminho do arquivo KML: ").strip()
    
    if not caminho_kml:
        print("Caminho do arquivo não fornecido")
        return
    
    if not os.path.exists(caminho_kml):
        print(f"Arquivo não encontrado: {caminho_kml}")
        return
    
    # Solicita delay entre requisições
    try:
        delay = input("Delay entre requisições em segundos (padrão: 1): ").strip()
        delay = float(delay) if delay else 1.0
    except ValueError:
        delay = 1.0
    
    # Confirma antes de processar
    print(f"\nConfiguração:")
    print(f"- Arquivo KML: {caminho_kml}")
    print(f"- Delay entre requisições: {delay}s")
    print(f"- API Endpoint: {converter.api_url}")
    
    confirmar = input("\nDeseja continuar? (s/n): ").strip().lower()
    if confirmar not in ['s', 'sim', 'y', 'yes']:
        print("Operação cancelada")
        return
    
    # Processa o arquivo
    converter.processar_arquivo_kml(caminho_kml, delay)

if __name__ == "__main__":
    main()