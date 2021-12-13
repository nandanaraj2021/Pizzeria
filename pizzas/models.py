from typing import Text
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Pizza(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name

# class Image(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images')

#     def __str__(self):
#         return self.title