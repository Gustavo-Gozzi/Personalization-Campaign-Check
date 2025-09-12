from domain.user import UserDomain

class UserService:
    @staticmethod
    def request_personalization(url, token, secret):
        new_user = UserDomain(url, token, secret)

        response = new_user.request_mcp()
        return data_validade(response)

    @staticmethod
    def data_validade(jason):

        response = {}

        if jason["campaignResponses"] and len(jason["campaignResponses"]) > 0:
            campaign = jason["campaignResponses"][0]
            experience_name = campaign["experienceName"]
            response["experiencie"] = experience_name

        else: 
            response["msg"] = 'Sem Experiencias'
        
        return response
