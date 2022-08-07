from click import option
from django.core.management.base import BaseCommand, CommandError
from blogdjango.models import Post 
from django.utils.text import slugify


class Command(BaseCommand):
    """Adds new post to the database.

    $ django-admin add_post --title "Post do terminal" --content "Postagem"
    """
    help = "Creates a new Post in the database."

    def add_arguments(self, parser):
        parser.add_argument("--title", type=str)
        parser.add_argument("--content", type=str)

    def handle(self, *args, **options):
        print(*args, options)
        try:
            post = Post.objects.create(
                title=options["title"],
                slug=slugify(options["title"]),
                content=options["content"],
            )
        except Exception as e:
            raise CommandError(e)    
        else: # se naõ deu o erro
            self.stdout.write(self.style.SUCCESS(f"Post {post.title} created."))
