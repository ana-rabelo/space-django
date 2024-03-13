from django.urls import path

from apps.usuarios.views import cadastro, login, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout')
]