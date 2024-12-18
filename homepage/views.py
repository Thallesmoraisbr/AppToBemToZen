from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from .models import ForumPergunta


# Create your views here.
def homepage_index(request):
    return render(request, 'homepage/index.html')

def homepage_cadastro(request):
    return render(request, 'homepage/cadastro.html')


def homepage_logout(request):
    if request.user.is_authenticated:
        logout(request)  
    return redirect('login')
    

def homepage_forum(request):
    # Busca todas as perguntas no banco
    perguntas = ForumPergunta.objects.all().order_by('-criado_em')
    return render(request, 'homepage/forum.html', {
        "perguntas": perguntas
    })

def homepage_forum_perguntas(request, pergunta_id):
    # TODO: Implementar o detalhe da pergunta e suas respostas
    # - Pergunta no topo com botão de Responder
    # - Listas de respostas
    pergunta = {}
    respostas = []
    return render(request, 'homepage/forum.html', {
        "pergunta": pergunta,
        "respostas": respostas
    })

def homepage_forum_reposta(request, pergunta_id):
    # TODO: Criar formulário para responder a pergunta
    return render(request, 'homepage/forum.html', {})