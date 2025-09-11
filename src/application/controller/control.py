from flask import jsonify, make_response, request
import UserDomain
from src.application.service import UserService
class Controller:
    @staticmethod
    def getData():
        data = request.get_json()

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

        user = UserService.request_personalization(data["url"], data["apiToken"], data["apiSecret"])
        return make_response(jsonify({"msg": "Deu certo"}), 200)

        



