import base64
import requests

class UserDomain:
    def __init__(self, url, APItoken, APIsecret, customer, expectedKeys):
        self.url = url
        self.APIToken = APItoken
        self.APIsecret = APIsecret
        self.code = f'Basic {self.encodeBasic()}'
        self.customer = customer
        self.expectedKeys = expectedKeys

    def encodeBasic(self):
        credentials = f'{self.APIToken}:{self.APIsecret}'
        credentials_byte = credentials.encode('utf-8')
        base = base64.b64encode(credentials_byte)
        base64_string = base.decode('utf-8')
        return base64_string

    def request_mcp(self, number_range=3):
        print(self.customer)
        header = {"Authorization":self.code}
        i = 0
        users = []
        for num in self.customer:
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
                            "userId": self.customer[0]['customerId']
                            },
                            "attributes": self.customer[0]['atributos']
                        }
                }
            r = requests.post(self.url, json=body, headers=header)
            users.append(r.json())
        return users   
          
    def to_dict(self):
        return {
            "url": self.url,
            "code": self.code
        }

