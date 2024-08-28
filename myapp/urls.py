from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL raiz chama a função 'index' de views
]