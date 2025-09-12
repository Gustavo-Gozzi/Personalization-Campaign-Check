import base64
import requests

class UserDomain:
    def __init__(self, url, APItoken, APIsecret):
        self.url = url
        self.APIToken = APItoken
        self.APIsecret = APIsecret
        self.code = f'Basic {self.encodeBasic()}'

    def encodeBasic(self):
        credentials = f'{self.APIToken}:{self.APIsecret}'
        credentials_byte = credentials.encode('utf-8')
        base = base64.b64encode(credentials_byte)
        base64_string = base.decode('utf-8')
        return base64_string

    def request_mcp(self, number_range=1):
        planinha = {
            "customerId": ['506679b17b6e5e28cadb3d93', '4e6679b17b6e5e28cadb3d93', 	'4f6679b17b6e5e28cadb3d93'],
            "attribute": "joke",
            "attributeValue": "hahaha"
        }
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
        header = {"Authorization":self.code}
        i = 0
        for i in range(number_range):
            body["user"]["identities"]["userId"] = planinha["customerId"][i]
            r = requests.post(self.url, json=body, headers=header)
            return r.json()   
          
    def to_dict(self):
        return {
            "url": self.url,
            "code": self.code
        }

