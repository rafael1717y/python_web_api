from flask import Flask, url_for, request
from flask_pymongo import PyMongo


app = Flask(__name__)


app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"
# Iniciliazando a extensão (recebe uma classe ou função 
# e a instância do app)
mongo = app.mongo = PyMongo(app)

@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config['APP_NAME']}"


# app.register_error_handler(404, not_found_page)


@app.route("/")
def index():
    posts = mongo.db.posts.find()  # generator (lazy) busca todos os posts
    #print(url_for("index"))
    # Retorna sempre código 200 por padrão ou se pode passar uma tupla com outro código.
    content_url = url_for("read_content", title="Novidades de 2022")
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2022</a>"
        "<hr>"
        f"{request.args}"
        f"{list(posts)}"
    )


@app.route("/<title>")
def read_content(title):
    index_url = url_for("index")
    return f"<h1>{title}</h1> <a href={index_url}>Voltar</a>"


# app.add_url_rule("/<title>", view_func=read_content)
