from django.shortcuts import render

def home(request):
    return render(request, 'curso/home.html')  # Página principal de curso

def formulario(request):
    return render(request, 'curso/formulario.html')  # Página del formulario
