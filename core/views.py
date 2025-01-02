from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')  # Renderiza la página principal

def about(request):
    return render(request, 'core/about.html')  # Renderiza la página "Acerca de"

