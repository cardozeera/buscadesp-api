from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS liberado para testes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou seu domínio frontend em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConsultaRequest(BaseModel):
    tipo: str  # nome, cpf3 ou telefone
    valor: str
    usuario: str

@app.post("/api/consulta-cpf")
def consultar(request: ConsultaRequest):
    return {
        "status": "ok",
        "dados": f"Resultado simulado para: /{request.tipo} {request.valor}",
        "pdf_url": "https://exemplo.com/arquivo.pdf",
        "txt_url": "https://exemplo.com/arquivo.txt"
    }


class ConsultaRequest(BaseModel):
    tipo: str  # nome, cpf3 ou telefone
    valor: str
    usuario: str

@app.post("/consultar")
def consultar(request: ConsultaRequest):
    return {
        "status": "ok",
        "dados": f"Resultado simulado para: /{request.tipo} {request.valor}",
        "pdf_url": "https://exemplo.com/arquivo.pdf",
        "txt_url": "https://exemplo.com/arquivo.txt"
    }
