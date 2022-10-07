from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import permissions
from . import permissions
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .serializers import OrderSerializer, StatusChangeSerializer
from .models import Order
from rest_framework.response import Response


# from .filters import ProductFilter


# Create your views here.

class OrderViewsSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    permission_classes = [permissions.IsAdminUser]  # must be is admin

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(customer=self.request.user)
        return self.queryset

    @action(methods=['POST'], detail=True, url_name='status-change', url_path='status-change')
    def status_change(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatusChangeSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Order Status has been changed!"}, status=status.HTTP_200_OK)
