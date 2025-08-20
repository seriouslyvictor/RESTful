from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Super API", description="Uma API para buscar todos os celulares disponíveis na loja", version="0.1.0")

class Produto(BaseModel):
    nome: str = Field(..., min_length=1, max_length=30, description="Nome do Produto")
    preco: float = Field(..., gt=0, description="Preço deve ser maior que zero")
    estoque: int = Field (..., ge=0, description="Estoque não pode ser negativo")
    id: int = Field(..., ge=0, description="ID deve ser um número positivo")

produtos = {
     0: Produto(nome="iPhone 16", preco=5999, estoque=6, id=0),   
     1: Produto(nome="Samsung Galaxy s23", preco=4999, estoque=8, id=1),   
     2: Produto(nome="Pocofone", preco=1999, estoque=12, id=3)
}

@app.get("/")
def root():
    return {
        "message": "Bem vindo à Super API!",
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": "todo..."
    }

@app.get("/produtos")
def listar_todos_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def buscar_item_por_id(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if produto_id in produtos:
        return produtos[produto_id]

@app.post("/produtos/")
def adicionar_produto(produto: Produto):
    if produto.id in produtos:
        raise HTTPException(status_code=409, detail=f"Produto com esse id {produto.id} já existe.")
    produtos[produto.id] = produto
    return f"Produto criado com sucesso, produto: {produto}"

@app.put("/produtos/{produto_id}")
def atualizar_produto_por_id(produto_id: int, nome: str | None = None, preco: float | None = None, estoque: int | None = None):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    
    produto = produtos[produto_id]
    campos_atualizados = []
    if nome:
        produto.nome = nome
        campos_atualizados.append("nome")
    if preco:
        produto.preco = preco
        campos_atualizados.append("preco")
    if estoque:
        produto.estoque = estoque
        campos_atualizados.append("estoque")
    
    return {
        "message": f"Produto {produto_id} atualizado com sucesso",
        "campos_atualizados": campos_atualizados,
        "produto": produto
    }

@app.delete("/produtos/{produto_id}")
def excluir_produto_por_id(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail=f"Um produto com esse id: {produto_id} não foi encontrado")
    
    excluido = produtos.pop(produto_id)
    return f"O produto {excluido} foi removido."

@app.get("/produtos/buscar/")
def buscar_produto_por_nome(nome: str):
    if not nome.strip():
        raise HTTPException(
            status_code=400,
            detail="Nome não pode ser vazio"
        )
    resultados =  [produto for produto in produtos.values() if nome.lower() in produto.nome.lower()]

    if not resultados:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum produto encontrado com o nome {nome}"
        )
    
    return {
        "total encontrados": len(resultados),
        "termo_busca": nome,
        "produtos": resultados
    }