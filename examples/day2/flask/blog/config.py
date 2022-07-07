import os
from dynaconf import FlaskDynaconf


# Pasta atual = pwd
HERE = os.path.dirname(os.path.abspath(__file__))


def configure(app):
    # ou start, init_app
    # Dynanconf procura arq. settings.toml e configura
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=HERE)
