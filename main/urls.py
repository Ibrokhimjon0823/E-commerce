from django.urls import path
from rest_framework.routers import SimpleRouter
from main.views import ProductListView, ProductDetailView, OrderViewSet

router = SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')
urlpatterns = router.urls


urlpatterns += [
    path("product/", ProductListView.as_view(), name="product-list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]


