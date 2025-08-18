import requests
import json

uri = "http://127.0.0.1:8000/"


resposta = requests.get(uri)
print(resposta.json())

# Adicionando um produto 
resposta1 = requests.post(uri, json={"nome": "Motorola Edge", "preco":1899, "estoque":4, "id":4})
print(resposta1.status_code)
print(resposta1.text)

# Atualizando um produto pelo endpoint + parametros
response = requests.put(f"{uri}produtos/0?preco=9000")
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

#Apagando um produto pelo endpoint por id
resposta3 = requests.delete(f"{uri}produtos/4")
print(f"Status: {resposta3.status_code}")
print(f"Response: {resposta3.text}")