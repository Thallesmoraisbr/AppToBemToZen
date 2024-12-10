from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# TODO: Criar model ForumPergunta
# Campos: 
# - pergunta text
# - criado_por User 

# TODO: Criar model ForumResposta com chave estrangeira para ForumPergunta
# Campos: 
# - pergunta ForumPergunta
# - resposta text
# - criado_por User
class ForumPergunta(models.Model):
    pergunta = models.TextField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pergunta[:50]

class ForumResposta(models.Model):
    pergunta = models.ForeignKey(ForumPergunta, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.TextField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resposta[:50]
