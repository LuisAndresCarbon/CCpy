from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('api.urls')),
    path('proyectos/', include('proyectos.urls')),
    path('activityarea/', include('SIG.ActivityArea.urls')),
    path('ped/', include('SIG.ped.urls')),
    path('ProjectAreaSig/', include('SIG.ProjectAreaSig.urls'))
]
