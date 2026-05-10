from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.book_controller import router as book_router

app = FastAPI(title="Livraria API - Exercício 8.3")

# Configuração do CORS - Essencial para a arquitetura Cliente-Servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # No deploy, trocaremos pelo link da Azure do front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas do controller
app.include_router(book_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API da Livraria Online rodando com sucesso!"}