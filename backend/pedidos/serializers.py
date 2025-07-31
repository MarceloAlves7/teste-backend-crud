from rest_framework import serializers
from .models import Produto, Pedido, ItemPedido
from django.db import transaction


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, write_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'data', 'status', 'itens']

    @transaction.atomic
    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item)
        return pedido
