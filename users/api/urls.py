from . import views
from django.urls import path

urlpatterns = [
    path('api_usuarios/', views.prueba, name='usuarios')
]
