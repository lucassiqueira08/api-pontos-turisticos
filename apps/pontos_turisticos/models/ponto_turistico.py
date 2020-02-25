from django.db import models

from apps.atracoes.models import Atracao
from apps.avaliacoes.models import Avaliacao
from apps.comentarios.models import Comentario
from apps.enderecos.models import Endereco


# Create your models here.


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    foto = models.ImageField(upload_to='img_pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.ForeignKey(
        'pontos_turisticos.DocumentoIdentificacao', on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
