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

    def request_mcp(self):
        planinha = dadosPlanilha() #criar essa funcao
        customersId = []
        for item in planinha:
            customersId.append(planinha[item])

        header = {"Authorization":self.code}
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
                    "userId": customerId
                    },
                    "attributes": {
                        attribute: attributeValue
                    }
                }
            }

            

    


    def to_dict(self):
        return {
            "url": self.url,
            "code": self.code
        }


