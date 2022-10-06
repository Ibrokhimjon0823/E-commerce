from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import OrderSerializer
from .models import Order
# from .filters import ProductFilter


# Create your views here.

class OrderViewsSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    permission_classes = [permissions.IsAuthenticated] ## must be is admin

    #
    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(self.__class__, self).get_permissions()
