from django.db import models

# Create your models here.

class Product_left(models.Model):
    name_left = models.CharField(max_length=20)
    small_price_left = models.CharField(max_length=20)
    big_price_left = models.CharField(max_length=20)
    image_left = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name_left

class Product_right(models.Model):
    name_right = models.CharField(max_length=20)
    small_price_right = models.CharField(max_length=20)
    big_price_right = models.CharField(max_length=20)
    image_right = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name_right