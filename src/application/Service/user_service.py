from src.Domain.user import UserDomain

class UserService:
    @staticmethod
    def request_personalization(url, token, secret):
        new_user = UserDomain(url, token, secret)

        response = new_user.request_mcp()
        return UserService.data_validade(response)

    @staticmethod
    def data_validade(lista):

        response = []
        for jason in lista:
            if jason["campaignResponses"] and len(jason["campaignResponses"]) > 0:
                campaign = jason["campaignResponses"][0]
                experience_name = campaign["experienceName"]
                user_name = jason['campaignResponses'][0]['payload']['Nome']
                user_lastname = jason['campaignResponses'][0]['payload']['Sobrenome']
                response.append(
                    {
                        "Nome": experience_name,
                        "Sobrenome": user_lastname,
                        "Experiencia": experience_name
                    }
                )

            else: 
                response["msg"] = 'Sem Experiencias'
        return response
