from django.urls import path
from . import views

app_name = 'appUsuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
]
