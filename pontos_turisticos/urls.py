from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename="pontoturistico")
router.register(r'atracoes', AtracaoViewSet, basename="atracoes")
router.register(r'enderecos', EnderecoViewSet, basename="enderecos")
router.register(r'comentarios', ComentarioViewSet, basename="comentarios")
router.register(r'avaliacoes', AvaliacaoViewSet, basename="avaliacoes")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
