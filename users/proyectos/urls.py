from django.urls import path
from .views import show_projects
urlpatterns = [
    path('show-projects/', show_projects, name='show_projects'),
    # Puedes agregar más URL según tus necesidades
]