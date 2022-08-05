from setuptools import setup

setup(
    name='django_blog',
    version='0.1.0',
    packages=["djblog", "blogdjango"],
    install_requires=[
        "django",
        "django-markdownify",
    ],
)

