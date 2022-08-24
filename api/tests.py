import json

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Product, ProductOrder

# Create your tests here.


class TestCrudProducts(APITestCase):

    def setUp(self):
        self.admin = User.objects.create(username="adminUser",
                                         password="testPassword", is_staff=True)
        self.user = User.objects.create(
            username="normUser", password="testPassword")

        self.user_token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)
        self.product = Product.objects.create(title="test", description="test description", price = 55)
        self.product_order = ProductOrder.objects.create(user=self.user,product=self.product)


    # Creating Updating Deleting Product as normal user
    def test_create_product_user(self):
        self.client.force_authenticate(user=self.user,token = self.user_token) 
        product = {
            "title": "moudr",
            "description": "madraaa",
            "price": "99.99"
        }

        response = self.client.post(reverse('product-list-create'), product)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_udpate_product_user(self):
        self.client.force_authenticate(user=self.user,token = self.user_token) 
        update = {
            "title": "update",
        }
        response = self.client.patch(
            reverse('product-update', kwargs={'pk': 1}), update)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    

    def test_delete_product_user(self):
        self.client.force_authenticate(user=self.user,token = self.user_token) 
        response = self.client.delete(
            reverse('product-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ################################################################################

    #Creating Updating Deleting Product as admin
    def test_create_product_admin(self):
        self.client.force_authenticate(user=self.admin,token = self.admin_token)
        product = {
            "title": "moudr",
            "description": "madraaa",
            "price": "99.99"
        }

        response = self.client.post(reverse('product-list-create'), product)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_udpate_product_admin(self):
        self.client.force_authenticate(user=self.admin,token = self.admin_token)
        update = {
            "title": "update",
        }
        response = self.client.patch(
            reverse('product-update', kwargs={'pk': 1}), update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "update")


    def test_delete_product_admin(self):
        self.client.force_authenticate(user=self.admin,token = self.admin_token)
        response = self.client.delete(
            reverse('product-delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #####################################################################################

    #Listing Products
    def test_list_products_all(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('product-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #####################################################################################

    #Purchasing and liting orders as User 

    def test_purchase_user(self):
        self.client.force_authenticate(user=self.user,token = self.user_token)
        response = self.client.post(
            reverse('product-purchase', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    
    def test_get_orders_user(self):
        self.client.force_authenticate(user=self.user,token = self.user_token)
        response = self.client.get(
            reverse('orders'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    #####################################################################################

    #Purchasing and liting orders as admin 

    def test_purchase_admin(self):
        self.client.force_authenticate(user=self.admin,token = self.admin_token)
        response = self.client.post(
            reverse('product-purchase', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_orders_admin(self):
        self.client.force_authenticate(user=self.admin,token = self.admin_token)
        response = self.client.get(
            reverse('orders'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

     