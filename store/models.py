from django.db import models

# Create your models here.
class Products(models.Model):

    name = models.TextField(verbose_name="product_name", max_length=255)