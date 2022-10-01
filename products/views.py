from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter


# Create your views here.
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductViewsSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [] ## must be is admin

    # def get_permissions(self):
    #     permissions = super().get_permissions()
    #     if self.action in ['list', 'retrieve']:
    #         return permissions.append(AllowAny())
    #     return permissions
    #
