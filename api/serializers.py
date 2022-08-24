import re
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product, ProductOrder


class ProductSerializer(serializers.ModelSerializer):
    purchase = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'purchase']

    #Displaying Purchase url    
    def get_purchase(self, obj):
        request = self.context.get('request') 
        if request is None:
            return None
        return reverse("product-purchase", kwargs={"pk": obj.pk}, request=request) 
    
    #Making Purchase url display only on Products List for normal users
    def to_representation(self, instance, **kwargs):
        user = self.context.get('request').user
        print(type(user))
        path = self.context.get('request').get_full_path()
        method = self.context.get('request').method
        match = re.search(r'\borders\b',path)

        if match or method in ['POST','PUT','PATCH'] or user.is_staff or user.is_anonymous:
            return {'title': instance.title, 'description': instance.description, 'price': instance.price }
        return super().to_representation(instance)

    


class ProductOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductOrder
        fields = ['user', 'product', 'created_at']
        extra_kwargs = {
            'user': {
                'write_only': True
            }
        }

