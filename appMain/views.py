from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appMain/index.html')

def nosotros(request):
    return render(request, 'appMain/nosotros.html')

def servicios(request):
    return render(request, 'appMain/servicios.html')