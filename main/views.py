from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from main import serializers
from main.models import Order, Product
from main import filters


# Create your views here.
class ProductListView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
