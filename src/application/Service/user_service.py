from src.Domain.user import UserDomain
import json


class UserService:
    @staticmethod
    def request_personalization(data):
        new_user = UserDomain(url=data["url"], APItoken=data["apiToken"], APIsecret=data["apiSecret"], 
        customer=data["customer"], expectedKeys=data["expectedKeys"])

        response = new_user.request_mcp()
        return UserService.data_validade(response, new_user.expectedKeys)

    @staticmethod
    def find_key(data_object, key_to_find):
    # Se for um dicionário, verifica as chaves
        if isinstance(data_object, dict):
            if key_to_find in data_object:
                return True
            # Se não encontrou na primeira camada, busca nos valores
            for value in data_object.values():
                if UserService.find_key(value, key_to_find):
                    return True
                    
        # Se for uma lista, itera sobre os itens
        elif isinstance(data_object, list):
            for item in data_object:
                if UserService.find_key(item, key_to_find):
                    return True
                    
        # Se não for dicionário nem lista, ou se a busca terminou sem sucesso
        return False

    @staticmethod
    def data_validade(lista, chaveEsperada):

        chaveEncontrada = False
        response = []
        for jason in lista:
            if jason["campaignResponses"] and len(jason["campaignResponses"]) > 0:

                if UserService.find_key(jason, chaveEsperada):
                    chaveEncontrada = True

                campaign = jason["campaignResponses"][0]
                experience_name = campaign["experienceName"]
                user_name = jason['campaignResponses'][0]['payload']['Nome']
                user_lastname = jason['campaignResponses'][0]['payload']['Sobrenome']

                response.append(
                    {
                        "Nome": user_name,
                        "Sobrenome": user_lastname,
                        "Experiencia": experience_name,
                        chaveEsperada: chaveEncontrada
                    }
                )


            else: 
                response["msg"] = 'Sem Experiencias'
        return response
