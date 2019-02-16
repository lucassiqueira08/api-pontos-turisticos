from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.avaliacoes.api.viewsets import AvaliacaoViewSet
from apps.comentarios.api.viewsets import ComentarioViewSet
from apps.enderecos.api.viewsets import EnderecoViewSet
from apps.pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from apps.atracoes.api.viewsets import AtracaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
