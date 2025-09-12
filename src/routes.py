from src.Application.Controller.user_control import Controller
from flask import jsonify, make_response

def teste():
    return Controller.getData()

def validation_routes(app):
    @app.route('/mcp/campaign', methods=['POST'])
    def validation():
        return Controller.getData()

if __name__ == '__main__':
    teste()