from django.urls import path
from .views import show_all_municipal
from .views import newProject_api_view, agregarProyecto

urlpatterns = [
    path('getnewProject/', newProject_api_view, name='getnewProject'),
    path('show-SigCats/',show_all_municipal, name='show_SigCats'),
      path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
 # Puedes agregar más URL según tus necesidades
]