import requests

def teste01():

    body = {
        "interaction": {
        "name": "teste usando python"
        },
        "source": {
            "channel": "Server",
            "application": "Campaign Teste Gustavo 1.0"
        },
        "user": {
            "identities":  {
            "userId": "506679b17b6e5e28cadb3d93"
            },
            "attributes": {
                "joke": "hahaha"
            }
        }
    }

    cabeca = {
        'Authorization': 'Basic QUFDRUUzOEUtRjdBNi00NDU5LUFBQ0EtMDI5OTA1RERBMDE1OmZFUXdvNVVIMUNLRDVDelc4bTJua2E0eWhmeVplbXN5LV9lajBraUN2NDQ='
    }
    r = requests.post('https://partnergentropbr.us-4.evergage.com/api2/authevent/grg_test', json=body, headers=cabeca)

    return r.json()


dicionario = {
    "msg": "oi",
    "otra": "tchau",
    "teste": "teste"
}

for item in dicionario:
    print(f"{item}: {dicionario[item]}")
