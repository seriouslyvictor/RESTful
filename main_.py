from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Super API", description="Uma API para buscar todos os celulares disponíveis na loja", version="0.1.0")

class Produto(BaseModel):
    nome: str
    preco: float
    estoque: int
    id: int

produtos = {
     0: Produto(nome="iPhone 16", preco=5999, estoque=6, id=0),   
     1: Produto(nome="Samsung Galaxy s23", preco=4999, estoque=8, id=1),   
     2: Produto(nome="Pocofone", preco=1999, estoque=12, id=3)
}