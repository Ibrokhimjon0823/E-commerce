from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import OrderViewsSet

router = SimpleRouter()
router.register('order', OrderViewsSet, basename='order')
# router.register('product', ProductViewsSet, basename='product')
urlpatterns = router.urls

