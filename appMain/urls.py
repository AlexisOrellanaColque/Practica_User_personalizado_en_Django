from django.urls import path
from . import views

app_name = 'appMain'

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'), 
    path('servicios/', views.servicios, name='servicios'),
]
