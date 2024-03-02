# blog/urls.py
from django.urls import path
from .views import blog_home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', blog_home, name='blog_home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
