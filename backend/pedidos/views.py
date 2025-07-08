from rest_framework import viewsets
from .models import Produto, Pedido
from .serializers import ProdutoSerializer, PedidoSerializer
from .pubsub.publisher import publish_pedido_created
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# from .pubsub import publish_pedido_created  # vamos criar em breve

class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        print("Dados do pedido recebidos:", self.request.data)

        pedido = serializer.save()
        publish_pedido_created(pedido.id)
