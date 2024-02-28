from django.urls import path
from .views import fncatversionaa,fnStatusValidacion
urlpatterns = [

    path('catversionaa/', fncatversionaa, name='catversionaa'),
    path('validacion/', fnStatusValidacion, name='validacion'),
    
 # Puedes agregar más URL según tus necesidades
]