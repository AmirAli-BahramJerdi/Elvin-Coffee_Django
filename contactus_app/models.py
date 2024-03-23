from django.db import models

# Create your models here.

class Massage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"