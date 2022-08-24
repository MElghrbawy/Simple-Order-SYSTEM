from django.urls import path

from .views import ProductListCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductOrderListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(),name='product-list-create'),
    path('products/<int:pk>/update', ProductUpdateAPIView.as_view(),name='product-update'),
    path('products/<int:pk>/delete', ProductDestroyAPIView.as_view(),name='product-delete'),
    #PURCHASE
    path('products/<int:pk>/purchase', ProductOrderListCreateAPIView.as_view(),name='product-purchase'),
    path('orders', ProductOrderListCreateAPIView.as_view(), name='orders')
]
