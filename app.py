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

planinha = {
            "customerId": [1, 3, 3],
            "attribute": "joke",
            "attributeValue": "hahaha"
        }

i = 0
number_range = 2
body = {
            "interaction": {
                "name": "Teste Campanha Server-Side"
                    },
                    "source": {
                        "channel": "Server",
                        "application": "Campaign Test"
                    },
                    "user": {
                        "identities":  {
                        "userId": "_"
                        },
                        "attributes": {
                            planinha["attribute"]: planinha["attributeValue"]
                        }
                    }
               }
for i in range(5):
    body["user"]["identities"]["userId"] = i
    print(body["user"]["identities"]["userId"])
    print(body["user"]["attributes"]["joke"])
