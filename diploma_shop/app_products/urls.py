from django.urls import path
from .api import ProductListView, CategoryView, CatalogView, ProductPopularView, ProductLimitedView, ProductSalesView, \
    ProductBannersView, TagsView, ProductDetailView, ReviewCreateView


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('products/popular', ProductPopularView.as_view(), name='products_popular'),
    path('products/limited', ProductLimitedView.as_view(), name='products_limited'),
    path('sales', ProductSalesView.as_view(), name='sales'),
    path('banners', ProductBannersView.as_view(), name='banners'),
    path('tags', TagsView.as_view(), name='tags'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/reviews', ReviewCreateView.as_view(), name='product_review'),
]
