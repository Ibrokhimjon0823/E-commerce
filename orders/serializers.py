from abc import ABC

from rest_framework import serializers
from models import Order, OrderDetails
from products.models import Product


class OrderProductSerializer(serializers.Serializer, ABC):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    count = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        products = validated_data.pop('products', [])
        order = super().create(validated_data)
        for product in products:
            OrderDetails.objects.create(
                order=order,
                product=product['product'],
                quantity=product['quantity'],
                price=product['product'].price
            )
        return order

    def update(self, instance, validated_data):
        super(OrderSerializer, self).update(instance, validated_data)

        for order_detail in self.instance.order_details.all():
            pass


        return instance
