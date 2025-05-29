# 📘 Conversor KML para API

## 🧩 Visão Geral

Este programa tem como objetivo **ler arquivos `.kml` contendo zonas geográficas**, processar os dados de coordenadas e **enviar essas zonas para a API** no formato esperado, com um preenchimento colorido aleatório (`fill_color`) no formato hexadecimal.

---

## ⚙️ Requisitos

- Python 3.7+
- `.env` com as variáveis de ambiente:
  - `BEARER_TOKEN`
  - `ACCOUNT_ID` (padrão: 621)
  - `API_URL`

### 📦 Bibliotecas utilizadas

```bash
pip install python-dotenv randomcolor requests
```

---

## 📁 Estrutura de Arquivos

```
Conversor V2.py
.env               # Arquivo de configuração com variáveis da API
zonas.kml          # Exemplo de arquivo de entrada KML
```

---

## 🔑 .env – Configuração

```env
# Token Bearer para autenticação na API
BEARER_TOKEN=seu_token_aqui

# ID da conta (padrão: 621)
ACCOUNT_ID=621
```

---

## 🚀 Como usar

1. **Execute o script**:

```bash
python Conversor\ V2.py
```

2. **Forneça o caminho para o arquivo `.kml`** quando solicitado.

3. **Defina o delay entre requisições** (recomendado: 1 segundo).

4. **Confirme a operação**.

---

## 🧠 Funcionamento interno

### 1. `extrair_placemarks_do_kml(caminho_arquivo)`

- Lê o XML do arquivo `.kml` e extrai todos os elementos `<Placemark>`.
- Retorna uma lista com nome e coordenadas brutas.

### 2. `processar_coordenadas(coordinates_text)`

- Converte a string de coordenadas em uma lista de pares `[lng, lat]`.
- Garante que o polígono seja fechado.

### 3. `criar_objeto(name, coordinates_array)`

- Gera:
  - ID automático baseado no nome e coordenadas.
  - Objeto JSON compatível com a API da Vuupt. (Podendo ser facilmente adaptado para outras API's alterando somente o método "criar_objeto")
  - **Cor aleatória em hexadecimal (`fill_color`)** usando `randomcolor`.

### 4. `enviar_para(zona_data)`

- Envia via `POST` para a URL:
  ```
  API_URL
  ```
- Autenticação via Bearer Token.

### 5. `processar_arquivo_kml(...)`

- Controla o fluxo completo: leitura do KML, conversão e envio.

---

## 🖌️ Exemplo de objeto enviado

```json
{
  "id": 12345,
  "account_id": 621,
  "name": "Zona A",
  "order": 0,
  "layer_type": "polygon",
  "coordinates": {
    "type": "Feature",
    "geometry": {
      "type": "Polygon",
      "coordinates": [[[-46.5, -23.5], [-46.6, -23.6], ...]]
    },
    "properties": []
  },
  "fill_color": "#ff337a"
}
```

---

## 🧪 Validações incluídas

- Checagem de existência e formato do arquivo `.kml`
- Verificação mínima de 3 coordenadas por zona
- Confirmação de polígono fechado
- Mensagens de erro detalhadas (parse, conexão, resposta da API)

---

## ✅ Exemplo de uso na prática

```bash
$ python Conversor\ V2.py

=== CONVERSOR KML PARA API ===

Digite o caminho do arquivo KML: zonas.kml
Delay entre requisições em segundos (padrão: 1):
...
Deseja continuar? (s/n): s

✅ Zona 'Bairro 1' enviada com sucesso (ID: 45873)
✅ Zona 'Bairro 2' enviada com sucesso (ID: 98233)

RESUMO: 2 zonas enviadas com sucesso, 0 falhas
```

---

## 🔐 Segurança

- O token nunca é hardcoded no código; é carregado de forma segura via `.env`.
- A biblioteca `dotenv` garante fácil configuração sem expor dados sensíveis.

---

## 🛠️ Manutenção futura

- Fácil adaptar para outras APIs com estrutura semelhante.
- Pode-se estender com logs em arquivos, logs para banco ou envio em lote.
