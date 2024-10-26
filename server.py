from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from index import *


app = FastAPI(title="Assistente IA", description="Um assistente para auxiliar no aprendizado de Python")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/gerar-questao/")
def apiGenerateQuestion(content: str):
    questao = generateQuestion(content)
    
    return {"questao": questao}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)