from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.atracoes.api.serializers import AtracaoSerializer
from apps.atracoes.models import Atracao
from apps.avaliacoes.api.serializers import AvaliacaoSerializer
from apps.comentarios.api.serializers import ComentarioSerializer
from apps.enderecos.api.serializers import EnderecoSerializer
from apps.enderecos.models import Endereco
from apps.pontos_turisticos.models import PontoTuristico, DocumentoIdentificacao


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocumentoIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    # Nested Relationships
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
            'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2', 'doc_identificacao'
        )
        read_only_fields = ('comentarios', 'avaliacoes')

    # Many to Many Nested Relationships - Para passar a atracao no body do request
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc_identificacao = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doc = DocumentoIdentificacao.objects.create(**doc_identificacao)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doc

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
