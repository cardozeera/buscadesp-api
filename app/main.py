from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
