from django.urls import path
from curso import views as curso_views

urlpatterns = [
    path('', curso_views.home, name='curso_home'),  # Página principal de curso
    path('formulario/', curso_views.formulario, name='curso_formulario'),  # Formulario
]
