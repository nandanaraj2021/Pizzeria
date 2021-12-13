from typing import Text
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Pizza(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

class Topings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()