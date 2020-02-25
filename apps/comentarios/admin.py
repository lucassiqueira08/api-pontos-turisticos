from django.contrib import admin

from apps.comentarios.actions import reprova_comentario, aprova_comentario
from apps.comentarios.models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentario, aprova_comentario]


# Register your models here.
admin.site.register(Comentario, ComentarioAdmin)
