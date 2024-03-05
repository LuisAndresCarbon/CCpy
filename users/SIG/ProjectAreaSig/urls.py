from django.urls import path
from .views import getAreaproject, getCatRan, fnctCertificacion, fngetctstatusvalidnap, fngetCatalogleadsig, fnprojectsAreas

urlpatterns = [
    path('getAreaproject/', getAreaproject, name='getAreaproject'),
    path('getctCertifi/', fnctCertificacion, name='getctCertifi'),
    path('catRan/', getCatRan, name='catRan'),
    path('getctstatusvalidnap/', fngetctstatusvalidnap, name='getctstatusvalidnap'),
    path('getctlead/', fngetCatalogleadsig, name= 'getctlead'),
    path('post/', fnprojectsAreas, name='post'),
]