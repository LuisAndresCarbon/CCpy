from django.urls import path
from .views import newProject_api_view, agregarProyecto, get_municipios, get_estados, get_ctagregation, get_ctNomNucleo, MunicipiosPorEstadoView, ShowDetailByMunicipality

urlpatterns = [
    path('getnewProject/', newProject_api_view, name='getnewProject'),
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('get_ctagregation/', get_ctagregation, name='get_ctagregation'),
    path('get_municipios/', get_municipios, name='get_municipios'),
    path('get_estados/', get_estados, name='get_estados'),
    path('get_NomNucleo/', get_ctNomNucleo, name='get_NomNucleo'),
    path('municipios/<int:Id_estado>/', MunicipiosPorEstadoView.as_view(), name='municipios-por-estado'),
    path('ShowDetailByMunicipality/<int:id_mun>/', ShowDetailByMunicipality.as_view(), name='ShowDetailByMunicipality'),
 # Puedes agregar más URL según tus necesidades
]