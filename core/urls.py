from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('cadastro/', cadastrar_usuario, name='cadastrar')
]