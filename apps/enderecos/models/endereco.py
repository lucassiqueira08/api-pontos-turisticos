from django.db import models


# Create your models here.
class Endereco(models.Model):
    logradouro = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=70, blank=True, null=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.logradouro

    def __repr__(self):
        return self.logradouro

