from django.db import models

# Create your models here.

class Coffee_left(models.Model):
    name_left = models.CharField(max_length=20)
    wight_left = models.CharField(max_length=20)
    price_left = models.CharField(max_length=20)
    image_left = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name_left


class Coffee_right(models.Model):
    name_right = models.CharField(max_length=20)
    wight_right = models.CharField(max_length=20)
    price_right = models.CharField(max_length=20)
    image_right = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name_right