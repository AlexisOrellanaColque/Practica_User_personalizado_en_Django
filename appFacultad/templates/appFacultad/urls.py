from django.urls import path
from appFacultad import views

app_name = 'appFacultad'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('facultades/', views.listar_Facultad, name='listar_facultad'),
    ]