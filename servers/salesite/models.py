from django.db import models

# Create your models here.
class Customers(models.Model):
    customer = models.CharField(max_length=32)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.EmailField()

class Servers(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

class PCs(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

class Laptops(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)


