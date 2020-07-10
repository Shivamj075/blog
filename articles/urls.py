
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:article_id>', views.detail, name='detail'),
]