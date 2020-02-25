from rest_framework.serializers import ModelSerializer
from apps.comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = (
            'id', 'usuario', 'comentario', 'data', 'aprovado'
        )
