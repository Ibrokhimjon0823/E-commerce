from rest_framework import serializers

from . import models
from .models import OrderProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name", "description")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = ("id", "payment_type")


class OrderProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())
    count = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, required=False)

    class Meta:
        model = models.Order
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        products = validated_data.pop('products', [])
        order = super().create(validated_data)
        for product in products:
            OrderProduct.objects.create(
                order=order,
                product=product['product'],
                count=product['count'],
                price=product['product'].price
            )
        return order

    # def update(self, instance, validated_data):
    #     pass
