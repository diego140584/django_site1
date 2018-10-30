from django.db import models
import time
from django.shortcuts import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    last_name = models.CharField(max_length=64,db_index=True)
    gender = models.CharField(max_length=10, null=True)
    birth = models.DateField(blank=True)
    role = models.CharField(max_length=32, blank=True)
    firm = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    date_registration = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=32)
    def __str__(self):
        return ("{} {}".format(self.name, self.last_name))

class Order(models.Model):
    date = models.DateField(time.asctime(time.localtime(time.time())))
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)

    def __str__(self):
        return ("{}".format(self.id + " " + self.customer))


class Server(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120, null=True)

    def __str__(self):
        return ("{}".format(self.model_name))

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)


class PC(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)

class Laptop(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)


