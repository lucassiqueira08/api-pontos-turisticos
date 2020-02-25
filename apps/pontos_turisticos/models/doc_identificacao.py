from django.db import models


class DocumentoIdentificacao(models.Model):
    descricao = models.CharField(max_length=100)
