from . import views
from django.urls import path
from .views import show_all, login

urlpatterns = [
    path('users/', show_all, name='user-list'),
    path('login/', login, name='login'),
]
