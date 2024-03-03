# blog/urls.py
from django.urls import path
from .views import post_list, add_post  # Ensure that add_post is correctly imported

urlpatterns = [
    path('', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
]
