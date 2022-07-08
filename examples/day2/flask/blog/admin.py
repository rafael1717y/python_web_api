from datetime import datetime
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required
from traitlets import default
from wtforms import form, fields, validators
from blog.database import mongo

# Monkey Patch 
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

# 1. Criação do formulário para o admin
class PostsForm(form.Form):
    title = fields.StringField("Title", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    content = fields.TextAreaField("Content")
    published = fields.BooleanField("Published", default=True)


# 2. Customização de quase td é aqui - ver doc
class AdminPosts(ModelView):
    column_list = ("title", "slug", "published", "date")
    
    form = PostsForm
    def on_model_change(self, form, post, is_created):
        post["slug"] = post["title"].replace("_", "-").replace(" ", "-").lower()
        # TODO: Criar função slugify (remover acentos)
        # TODO: Verificar se o post com o mesmo slug já existe
        if is_created:
            post["date"] = datetime.now()

        



def configure(app):
    admin = Admin(
        app,
        name=app.config.get("TITLE"),
        template_mode="bootstrap4"
    )
    # 3 - recebe a collections (mongo.db.posts)
    admin.add_view(AdminPosts(mongo.db.posts, "Posts"))


# TODO: criar formulário para cadastro de usuários. 
