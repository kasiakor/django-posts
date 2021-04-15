from django.contrib import admin
from django.urls import path

from posts.views import post_list_view

# add tyhe view, function will be invoked at this url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list_view)
]
