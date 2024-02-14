from django.urls import path
from .views import newProject_api_view, agregarProyecto, get_municipios, get_estados, get_ctagregation, get_ctNomNucleo, MunicipiosPorEstadoView,get_projects,post_projects,get_municipalities, get_Agrario
urlpatterns = [
    path('getnewProject/', newProject_api_view, name='getnewProject'),
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('get_ctagregation/', get_ctagregation, name='get_ctagregation'),
    path('get_municipios/', get_municipios, name='get_municipios'),
    path('get_NomNucleo/', get_ctNomNucleo, name='get_NomNucleo'),
    path('municipios/<int:Id_estado>/', MunicipiosPorEstadoView.as_view(), name='municipios-por-estado'),
    
    path('Agrario/<int:id_mun>/', get_Agrario, name='Agrario'),
    path('municipalities/<int:id_Estado>/',get_municipalities, name='municipalities'),
    path('get_estados/', get_estados, name='get_estados'),
    path('get_projects/', get_projects, name='get_projects'),
    path('post_projects/', post_projects, name='post_projects'),
 # Puedes agregar más URL según tus necesidades
]