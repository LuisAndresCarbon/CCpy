from . import views
from django.urls import path
from .views import show_all, login

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/', show_all , name='user-list'),
    path('login/', login, name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
