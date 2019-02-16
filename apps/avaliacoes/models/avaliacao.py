from django.contrib.auth.models import User
from django.db import models


# Create your models here
class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username

    def __repr__(self):
        return self.usuario.username
