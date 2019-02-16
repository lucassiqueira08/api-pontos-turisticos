from rest_framework.serializers import ModelSerializer
from apps.enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'logradouro', 'bairro', 'cidade', 'estado', 'numero', 'cep', 'complemento', 'pais', 'latitude', 'longitude'
        )
