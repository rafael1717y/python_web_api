from __future__ import annotations
from blog.database import mongo
from datetime import datetime



def get_all_posts(published: bool =True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")



def get_post_by_slug(slug: str) -> dict:
    """/Novidades%20%de2022
       /Novidades de 2022 
       /novidades-de-2022 
    """
    post = mongo.db.posts.find_one({"slug": slug})
    return post 



def update_post_by_slug(slug: str, data: dict) -> dict:
    """Atualiza pelos dados encontrados pelo data $set:data """
    # TODO: Se o título mudar, atualizar o slug (falhar se já existir) 
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    # TODO: Refatorar a criação do slug removendo acentos 
    slug = title.replace(" ", "-").replace("_", "-").lower()
    # TODO: Verificar se post com este slug já existe

    # Mongo não commit, session.
    new = mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content, 
            "published": published,      
            "slug": slug, 
            "date": datetime.now(),       
        }
    )
    return slug


def delete_post(title: str, content:str, published: bool = True) -> str:
    pass
