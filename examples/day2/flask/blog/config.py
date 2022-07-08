import os
from dynaconf import FlaskDynaconf


# Pasta atual = pwd
HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", 5000))

def configure(app):
    # ou start, init_app
    # Dynanconf procura arq. settings.toml e configura
    app.config["PORT"] = PORT
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=HERE)
