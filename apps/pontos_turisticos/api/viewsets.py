# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # Mecanismo de Autorização
    permission_classes = (IsAuthenticated,)
    # IsAuthenticatedOrReadOnly
    authentication_classes = (TokenAuthentication,)

    filter_backends = (DjangoFilterBackend, SearchFilter)
    # Permite que seja filtrado por nome e descricao
    filter_fields = ('nome', 'descricao')

    # Permite que seja feita uma busca por nome e descricao
    search_fields = ('nome', 'descricao')

    # Lookup field permite que seja feita uma pesquisa via url de um
    # campo como se fosse um ID, porém deve-se garantir a unicidade.
    # lookup_field = 'nome'

    def get_queryset(self):
        """
        Função nativa que pode ser sobrescrita para substituir o queryset,
        possibilita o filtro de dados de forma mais robusta.

        """
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        """
        Função nativa que pode ser sobrescrita, quando a API recebe um GET para listar nesse endpoint,
        essa função é responsável por devolver os objetos
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Função nativa responsavel pelo metodo POST, pode ser sobrescrita.
        """
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Função nativa responsável pelo método DELETE, pode ser sobrescrita.
        """
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Função nativa responsavel pelo metodo GET porem de um recurso específico
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Função nativa responsavel pelo metodo PUT, atualiza um recurso específico
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Função nativa responsavel pelo metodo PATCH, atualiza uma parte de um recurso específico

        """
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def action_customizada(self, request, pk=None):
        """
        Action customizada acessível chamando a url:
        http://localhost:8000/pontosturisticos/1/action_customizada

        methods define com quais metodos essa action sera chamada
        detail = True define que o request trará os detalhes do recurso, como por exemplo a pk.
        """
        pass

    @action(methods=['get'], detail=False)
    def action_customizada_sem_detalhes(self, request):
        """
        Action customizada acessível chamando a url:
        http://localhost:8000/pontosturisticos/action_customizada_sem_detalhes
        """
        pass
