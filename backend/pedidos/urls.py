from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, PedidoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
