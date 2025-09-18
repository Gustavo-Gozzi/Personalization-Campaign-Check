import json

# Seu JSON como uma string multi-linha
data = {
    "id": "68c9aa3c968a72592a6803b2",
    "campaignResponses": [
        {
            "type": "ng",
            "campaignId": "7CZ31",
            "campaignName": "Campaign Teste Gustavo 1.0",
            "campaignType": "ServerSide",
            "experienceId": "IDJlO",
            "experienceName": "Experience 1",
            "experienceSourceCode": "",
            "state": "Published",
            "campaignJavascriptContent": None,
            "userGroup": "Default",
            "templateNames": [
                "Teste-GustavoGozziTemplate"
            ],
            "payload": {
                "product": {
                    "id": "NAVE00A01",
                    "location": None,
                    "attributes": {
                        "productWeight": { "value": None },
                        "inventoryCount": { "value": 0 },
                        "name": { "value": "Millenniun Falcon" },
                        "price": { "value": 1.0E12 },
                        "promotable": { "value": True },
                        "productName": { "value": None },
                        "imageUrl": { "value": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvhDU8BwPkW2hmqk6KAj02zd2ekdNS2nrI0l-f3hqOPw&s" },
                        "archived": { "value": False },
                        "url": { "value": "" },
                        "description": { "value": "Nave espacial Millennium Falcon\\n\\nAPENAS PARA TESTES, NÃO REPRESENTA UM PRODUTO DE VERDADE OU UMA VENDA REAL" }
                    },
                    "dimensions": {
                        "CatalogObjectColor": [ "COLOR000C2", "COLOR000C0" ],
                        "CatalogObjectGender": [ "Gender001" ],
                        "LadoForca": [ "LDF000F1" ]
                    },
                    "categories": [],
                    "skus": {}
                },
                "productId": "NAVE00A01",
                "subtitle": "Joker",
                "campaign": "7CZ31",
                "title": "Este é o Coringa",
                "experience": "IDJlO",
                "userGroup": "Test",
                "Sobrenome": "Jones",
                "Nome": "Indiana"
            }
        }
    ],
    "errorCode": 0,
    "resolvedUserId": "506679b17b6e5e28cadb3d93"
}


# 1. Converter a string JSON para um objeto Python (dicionário/lista)
#data = json.loads(json_string)

# 2. Função recursiva para procurar a chave
def find_key(data_object, key_to_find):
    
    # Se for um dicionário, verifica as chaves
    if isinstance(data_object, dict):
        if key_to_find in data_object:
            return True
        # Se não encontrou na primeira camada, busca nos valores
        for value in data_object.values():
            if find_key(value, key_to_find):
                return True
                
    # Se for uma lista, itera sobre os itens
    elif isinstance(data_object, list):
        for item in data_object:
            if find_key(item, key_to_find):
                return True
                
    # Se não for dicionário nem lista, ou se a busca terminou sem sucesso
    return False

# --- Testando a função ---

# Procurando pela chave "Nome"
key_to_search = "Nome"
if find_key(data, key_to_search):
    print(f"A chave '{key_to_search}' foi encontrada no JSON.")
else:
    print(f"A chave '{key_to_search}' NÃO foi encontrada no JSON.")

# Testando com outra chave que também existe ("productWeight")
if find_key(data, "productWeight"):
    print("A chave 'productWeight' foi encontrada no JSON.")
else:
    print("A chave 'productWeight' NÃO foi encontrada no JSON.")

# Testando com uma chave que não existe
if find_key(data, "Idade"):
    print("A chave 'Idade' foi encontrada no JSON.")
else:
    print("A chave 'Idade' NÃO foi encontrada no JSON.")