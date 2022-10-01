# import django_filters
#
# from main.models import Product, Category
#
#
# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Product
#         fields = ['name', 'country', 'brand']
#
#
# class CategoryFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Category
#         fields = ['name']
