from rest_framework import serializers

from . import models


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


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = "__all__"
