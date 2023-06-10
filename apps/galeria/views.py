from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)  
    return render(request, 'galeria/index.html', {"cards": fotografias})
    
def imagem(request, foto_id): # Recebe os parâmetros da requisição
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    Fotografia.objects.filter(pk=foto_id).update(quantidade_visitas = (fotografia.quantidade_visitas + 1))
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def mais_vistas(request):
    fotografias = Fotografia.objects.order_by("-quantidade_visitas").filter(publicado=True)  
    return render(request, 'galeria/index.html', {"cards": fotografias})