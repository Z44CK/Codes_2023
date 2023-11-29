from django.contrib import admin
from django.urls import path, include
from .views import operacao_matematica
from rest_framework import permissions
from drf_yasg import get_schema_view
from drf_yasg import openapi
from api.views import operacao_matematica

schema_view = get_schema_view(
    openapi.Info(
        title="API de Operação matematica",
        default_version='v1',
        description="API para realizar operações matematicas",
        terms_of_service="https://www.meuapp.com/terms",
        contact=openapi.Contact(email='julianomlp@hotmail.com'),
        license=openapi.License(name='minha licença'),
    ),
    public=True,
    permissions_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('operacao-matematica/', operacao_matematica, name='operacao-matematica'),
    path('swaggers/', schema.view_ui('swaggers', cache_timeout=0), name='schema-swaggers-ui'),
]
