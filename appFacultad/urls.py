from django.urls import path
from . import views

app_name = 'appFacultad'

urlpatterns = [
    path('', views.home, name='home'),
    path('facultades/', views.listar_facultad, name='listar_facultad'),
]