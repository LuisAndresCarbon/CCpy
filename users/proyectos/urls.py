from django.urls import path
from .views import get_estados,get_projects,post_projects,get_municipalities, get_Agrario, getaggregation, getprojecthist, fnprojectshist,fnCtnostifyProjecthist
urlpatterns = [

    path('agrario/<int:id_mun>/', get_Agrario, name='agrario'),
    path('municipalities/<int:id_Estado>/',get_municipalities, name='municipalities'),
    path('get_estados/', get_estados, name='get_estados'),
    path('getaggregation/', getaggregation, name='getaggregation'),
    path('get_projects/', get_projects, name='get_projects'),
    path('post_projects/', post_projects, name='post_projects'),
    path('setprojecthist/<int:project_id>/',getprojecthist, name='setprojecthist'),
    path('spprojectshist/', fnprojectshist, name='spprojectshist'),
    path('spprojectshist/', fnprojectshist, name='spprojectshist'),
    path('ctNotify/', fnCtnostifyProjecthist, name='ctNotify'),
    
]