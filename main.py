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

@app.get("/")
def indice():
    return produtos

@app.get("/produtos/{produto_id}")
def buscar_item_por_id(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if produto_id in produtos:
        return produtos[produto_id]
    
@app.get("/produtos/")
def buscar_produto_por_nome(nome: str):
    return [produto for produto in produtos.values() if nome.lower() in produto.nome.lower()]

@app.post("/")
def adicionar_produto(produto: Produto):
    if produto.id in produtos:
        raise HTTPException(status_code=400, detail=f"Produto com esse id {produto.id} já existe.")
    produtos[produto.id] = produto
    return f"Produto adicionado {produto}"

@app.put("/produtos/{produto_id}")
def atualizar_produto_por_id(produto_id: int, nome: str | None = None, preco: float | None = None, estoque: int | None = None):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    
    produto = produtos[produto_id]
    if nome:
        produto.nome = nome
    if preco:
        produto.preco = preco
    if estoque:
        produto.estoque = estoque
    
    return f"Produto {produto_id} atualizado"

@app.delete("/produtos/{produto_id}")
def excluir_produto_por_id(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail=f"Um produto com esse id: {produto_id} não foi encontrado")
    
    excluido = produtos.pop(produto_id)
    return f"O produto {excluido} foi removido."