from django.urls import path
from galeria.views import index, imagem, buscar, mais_vistas


urlpatterns = [
        path('', index, name='index'),
        path('imagem/<int:foto_id>', imagem, name='imagem'),
        path('buscar', buscar, name='buscar'),
        path('mais_vistas', mais_vistas, name='mais_vistas')
] 