from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from apps.atracoes.api.viewsets import AtracaoViewSet
from apps.avaliacoes.api.viewsets import AvaliacaoViewSet
from apps.comentarios.api.viewsets import ComentarioViewSet
from apps.enderecos.api.viewsets import EnderecoViewSet
from apps.pontos_turisticos.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
# base_name define qual o model que deve ser apontado.
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('api-token-auth/', obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
