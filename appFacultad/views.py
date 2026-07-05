from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'appFacultad/home.html')

def listar_facultad(request):
    return render(request, 'appFacultad/listar_facultad.html')