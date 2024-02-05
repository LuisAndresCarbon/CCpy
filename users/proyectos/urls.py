from django.urls import path
from .views import newProject_api_view, agregarProyecto, get_municipios, get_estados, get_ctagregation

urlpatterns = [
    path('getnewProject/', newProject_api_view, name='getnewProject'),
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('get_ctagregation/', get_ctagregation, name='get_ctagregation'),
    path('get_municipios/', get_municipios, name='get_municipios'),
    path('get_estados/', get_estados, name='get_estados'),

 # Puedes agregar más URL según tus necesidades
]