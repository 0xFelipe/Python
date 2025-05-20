from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
import httpx
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL", "https://api.vuupt.com/api/v1")

app = FastAPI(title="Serviços CRUD")

# Configuração de templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cabeçalhos HTTP para as requisições à API
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Classes para validação de dados
class Address(BaseModel):
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class Customer(BaseModel):
    name: str
    email: str
    upsert: bool = True
    address: Optional[str] = None
    phone_number: Optional[str] = None
    address_complement: Optional[str] = None

class Service(BaseModel):
    code: str
    note: str
    type: str  # "delivery" ou "pickup"
    title: str
    upsert: bool = True
    address: str
    latitude: float
    longitude: float
    customer_id: Optional[str] = None
    customer: Optional[Customer] = None
    driver_id: Optional[str] = None

# Rotas
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renderiza a página principal."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/contatos")
async def get_contatos():
    """Retorna a lista de clientes da API."""
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            print(f"Fetching customers from: {BASE_URL}/customers")
            response = await client.get(f"{BASE_URL}/customers", headers=headers)
            response.raise_for_status()  # Vai lançar exceção para códigos de erro HTTP
            data = response.json()
            
            # Log da resposta para debug
            print(f"API Response: {data}")
            
            return data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, 
                           detail=f"Erro na API externa: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, 
                           detail=f"Erro ao buscar clientes: {str(e)}")

@app.get("/api/drivers")
async def get_drivers():
    """Retorna a lista de motoristas da API."""
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            print(f"Fetching drivers from: {BASE_URL}/agents")
            response = await client.get(f"{BASE_URL}/agents", headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # Log da resposta para debug
            print(f"API Response: {data}")
            
            return data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, 
                           detail=f"Erro na API externa: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, 
                           detail=f"Erro ao buscar motoristas: {str(e)}")

@app.get("/api/geocode/{address}")
async def geocode_address(address: str):
    """Geocodifica um endereço usando a API."""
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            print(f"Geocoding address at: {BASE_URL}/utilities/map/geocode with address={address}")
            response = await client.get(
                f"{BASE_URL}/utilities/map/geocode",
                headers=headers,
                params={"address": address}
            )
            response.raise_for_status()
            data = response.json()
            
            # Log da resposta para debug
            print(f"API Response: {data}")
            
            return data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, 
                           detail=f"Erro na API externa: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, 
                           detail=f"Erro ao geocodificar endereço: {str(e)}")

@app.post("/api/services")
async def create_service(service: Union[Service, Dict[str, Any]]):
    """Cria um novo serviço."""
    try:
        # Se recebemos um dicionário em vez do modelo Pydantic
        service_data = service if isinstance(service, dict) else service.dict(exclude_none=True)
        
        # Log dos dados antes de enviar
        print(f"Posting service to: {BASE_URL}/services")
        print(f"Service data: {json.dumps(service_data, indent=2)}")
        
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{BASE_URL}/services",
                headers=headers,
                json=service_data
            )
            response.raise_for_status()
            data = response.json()
            
            # Log da resposta para debug
            print(f"API Response: {data}")
            
            return data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, 
                           detail=f"Erro na API externa: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, 
                           detail=f"Erro ao criar serviço: {str(e)}")

# Executar o servidor
if __name__ == "__main__":
    import uvicorn
    print(f"Starting server with BASE_URL: {BASE_URL}")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)