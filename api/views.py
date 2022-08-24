from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response

from .models import Product, ProductOrder
from .serializers import ProductSerializer,ProductOrderSerializer
from .permissions import AdminCreatePermission, NormalUserPermission


#PRODUCTS API
class ProductListCreateAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminCreatePermission]


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]

#PURCHASE API

class ProductOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    permission_classes = [permissions.IsAuthenticated, NormalUserPermission]

    #Creating product order
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        user=self.request.user
        product = get_object_or_404(Product, pk=pk)
        if user and product:
            serializer.save(user=user,product=product)
               
    #Getting authinticated user products 
    def get_queryset(self): 
        qs = super().get_queryset()
        request=self.request
        return qs.filter(user=request.user)
    
        
