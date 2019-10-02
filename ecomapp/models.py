from django.db import models
from datetime import datetime
from django.conf import settings
from django.db import models


# Create your models here.

class Category(models.Model):
    #category_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    category_id = models.AutoField
    category_name = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.category_name


class Product(models.Model):
    #prod_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,)
    product_id = models.AutoField
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='ecomapp/images', default="")

    def __str__(self):
        return self.product_name


class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=15, default="")
    #order_name = models.CharField(max_length=50, default="")
    mobile_No = models.IntegerField(default=0)
    password = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.user_name

class Order(models.Model):
    order_id = models.AutoField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    order_date = models.DateField()

    # def __str__(self):
    #     return self.order_id

class Cart(models.Model):
    cart_id = models.AutoField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)


    # def __str__(self):
    #     return self.cart_id