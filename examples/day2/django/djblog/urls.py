from django.contrib import admin
from django.urls import path
from django.contrib import admin 
from django.urls import path
from blogdjango.views import new_post, PostDetail, PostList


urlpatterns = [
    path('admin/', admin.site.urls),
    path("new/", new_post, name="new_post"),
    path("", PostList.as_view(), name="index"),
    path("<slug:slug>/", PostDetail.as_view(), name="detail"),
]
