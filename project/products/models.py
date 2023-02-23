from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1231, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=123)
    
    def __str__(self):
        return self.name

