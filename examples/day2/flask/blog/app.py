from flask import Flask
from blog.config import configure  # o app import o plugin (inversão de controle)




def create_app():
    app = Flask(__name__)
    configure(app)
    return app
