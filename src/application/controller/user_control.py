from flask import jsonify, make_response, request
from src.Application.Service.user_service import UserService
class Controller:
    @staticmethod
    def getData():
        data = {
            'url': 'https://partnergentropbr.us-4.evergage.com/api2/authevent/grg_test',
            'apiToken': 'AACEE38E-F7A6-4459-AACA-029905DDA015',
            'apiSecret': 'fEQwo5UH1CKD5CzW8m2nka4yhfyZemsy-_ej0kiCv44',
            'customer': [{
                        "customerId": '506679b17b6e5e28cadb3d93',
                        'atributos': {
                        "joke": "hahaha"
                        } 
                    },
                    {
                        "customerId": '4f6679b17b6e5e28cadb3d93',
                        'atributos': {
                        "joke": "batima"
                        } 
                    },
                    {
                        "customerId": '4e6679b17b6e5e28cadb3d93',
                        'atributos': {
                        
                        } 
                    }],
            'expectedKeys': 'Nome'

        }#request.get_json()

        required_data = ["url", "apiToken", "apiSecret"]
        missed_data = []
        for item in required_data:
            if item not in data:
                missed_data.append(item)

        if missed_data:
            return make_response(jsonify({"erro": f"Estão faltando os seguintes campos: {missed_data}"}), 400)

        required_url_caractere = ['https', ':', '/', 'evergage', 'authevent', 'api', '.com']
        missed_url_caractere = []
        for item in required_url_caractere:
            if item not in data["url"]:
                missed_url_caractere.append(item)

        if missed_url_caractere:    
            return make_response(jsonify({"erro": f"Estão faltando os seguintes caracteres na URL: {missed_url_caractere}"}), 400)

        
        user = UserService.request_personalization(data)
        return {"msg": "Deu certo", "response": user}#make_response(jsonify({"msg": "Deu certo", "response": user}), 200)

        



