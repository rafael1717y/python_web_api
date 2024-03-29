from django.contrib.auth.decorators import login_required
from django.forms import ModelForm 
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse
from django.utils.text import slugify
from blogdjango.models import Post
from django.views.generic import ListView, DetailView, CreateView


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']



@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():  # valida cfe o model.
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return HttpResponseRedirect(reverse("index"))
    else: 
        form = PostForm()

    return render(request, "new_post.html", {"form": form})


class PostList(ListView):
    #decorations = [login_required]  # for class based view
    model = Post 
    template_name = "index.html"
    queryset = Post.objects.filter(published=True)  #List view para mostrar posts = True.    


class PostDetail(DetailView):
    model = Post
    template_name = "detail.html"

