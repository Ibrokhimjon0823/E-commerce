from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductViewsSet

router = SimpleRouter()
# router.register(r'order', OrderViewSet, basename='order')
router.register('product', ProductViewsSet, basename='product')
urlpatterns = router.urls

