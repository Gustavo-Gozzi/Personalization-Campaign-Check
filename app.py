from src.routes import teste
from flask import Flask

def create_app():
    app = Flask(__name__)

    register_routes(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)