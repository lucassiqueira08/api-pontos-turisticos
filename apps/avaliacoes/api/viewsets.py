from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from apps.avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # Mecanismo de Autorização
    permission_classes = (IsAuthenticated,)
    # IsAuthenticatedOrReadOnly
    authentication_classes = (TokenAuthentication,)

