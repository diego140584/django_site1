from django.db import models
import time

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    gender = models.CharField(max_length=10, null=True)
    birth = models.DateField(null=True)
    role = models.CharField(max_length=32)
    firm = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    date_registration = models.DateTimeField(null=True)
    password = models.CharField(max_length=32, null=True)
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


class PC(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)

class Laptop(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    date = models.DateField("date arrives")
    description = models.TextField(max_length=120)


