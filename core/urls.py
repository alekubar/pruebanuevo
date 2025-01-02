from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),  # Página principal de core
    path('about/', core_views.about, name='about'),  # Página "Acerca de"
    path('curso/', include('curso.urls')),  # Incluir las URLs de curs
]