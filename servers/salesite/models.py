from django.db import models

# Create your models here.
class Customer(models.Model):
    customer = models.CharField(max_length=32)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.EmailField()

class Server(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

class PC(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

class Laptop(models.Model):
    customer = models.ForeignKey(Customers)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)


