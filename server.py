from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from index import generateQuestion

app = FastAPI(title="Assistente IA", description="Um assistente para auxiliar no aprendizado.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    content: str

@app.post("/gerar-questao/")
async def api_generate_question(request: QuestionRequest):
    questao = generateQuestion(request.content)
    # Suponha que a função generateQuestion retorna um dicionário com 'questao', 'alternativas' e 'resposta_correta'
    if not questao:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    return {
        "questao": questao,  # Ajuste conforme a estrutura esperada
        "alternativas": ["Alternativa 1", "Alternativa 2", "Alternativa 3", "Alternativa 4"],  # Exemplo
        "resposta_correta": "Alternativa 1"  # Exemplo
    }
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

