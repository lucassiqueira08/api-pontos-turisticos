from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from apps.enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    # Mecanismo de Autorização
    permission_classes = (IsAuthenticated,)
    # IsAuthenticatedOrReadOnly
    authentication_classes = (TokenAuthentication,)
