from django.urls import path
from .views import fnCatresultpedAP,fnCatseccionAA,fnCatpoblacionAA,fnCatActivityAG,fnCatActivityAG, fnCatEncuestas, fnCatsubSidiosAA, fnCatPendienteAA,fnCatChangeofCoverage, fnresultPedAA
urlpatterns = [

    path('resultAp/', fnCatresultpedAP, name='resultAp'),
    path('ctseccionAA/', fnCatseccionAA, name='ctseccionAA'),
    path('ctpoblacionAA/', fnCatpoblacionAA, name='ctpoblacionAA'),
    path('ctActivityAG/', fnCatActivityAG, name='ctActivityAG'),
    path('ctEncuestas/', fnCatEncuestas, name='ctEncuestas'),
    path('ctsubSidiosAA/', fnCatsubSidiosAA, name='ctsubSidiosAA'),
    path('ctPendienteAA/', fnCatPendienteAA, name='ctPendienteAA'),
    path('ctChangeofCoverage/', fnCatChangeofCoverage, name='ctChangeofCoverage'),
    path('ctresultPedAA/', fnresultPedAA, name='ctresultPedAA')
 # Puedes agregar más URL según tus necesidades
]