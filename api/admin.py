from django.contrib import admin
from .models import Product, ProductOrder

admin.site.register(Product)
admin.site.register(ProductOrder)