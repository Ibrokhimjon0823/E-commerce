from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from main import serializers
# from main.models import Order, Product
from main import filters


# Create your views here.
# class ProductListView(generics.ListAPIView):
#     serializer_class = serializers.ProductSerializer
#     queryset = Product.objects.all()
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = filters.ProductFilter
#
#
# class ProductDetailView(generics.RetrieveAPIView):
#     serializer_class = serializers.ProductSerializer
#     queryset = Product.objects.all()


# class ProductViewsSet(viewsets.ModelViewSet):
#     serializer_class = serializers.ProductSerializer
#     queryset = Product.objects.all()
#     permission_classes = [] ## must be is admin

    # def get_permissions(self):
    #     permissions = super().get_permissions()
    #     if self.action in ['list', 'retrieve']:
    #         return permissions.append(AllowAny())
    #     return permissions


# class OrderViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderSerializer
