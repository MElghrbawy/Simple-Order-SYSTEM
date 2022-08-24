from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=1)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True , on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    