from rest_framework import serializers
from .models import Order, OrderDetails
from products.models import Product


class OrderProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, required=False)
    order_details = OrderProductSerializer(many=True, required=False)

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
        products = validated_data.pop('products', [])
        order = super().update(instance, validated_data)
        pk_list = []
        for product in products:
            pk_list.append(product['product'].pk)
            OrderDetails.objects.update_or_create(
                order=order,
                product=product['product'],
                defaults=dict(
                    quantity=product['quantity'],
                    price=product['product'].price
                )
            )
        OrderDetails.objects.exclude(order=order, product_id__in=pk_list).delete()

        return instance
