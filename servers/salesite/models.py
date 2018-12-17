from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model



# Create your models here.
usr = get_user_model()


class Customer(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    last_name = models.CharField(max_length=64, db_index=True,)
    login = models.CharField(max_length=32, db_index=True, null=True)
    gender = models.CharField(max_length=10, null=True)
    birth = models.DateField(blank=True,auto_now_add=False)
    firm = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    date_registration = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['-date_registration']


    def __str__(self):
        return ("{} {}".format(self.name, self.last_name))



class Server(models.Model):

    model_name = models.CharField(max_length=64, verbose_name='Name')
    cost = models.FloatField(null=True,verbose_name="Price")
    quantity = models.IntegerField(default=0,verbose_name="Quantity")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    description = models.TextField(max_length=120, null=True, verbose_name='Description')
    image = models.ImageField(blank=True, verbose_name='Image')


    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"
        ordering = ['-date']


    def __str__(self):
        return ("{}".format(self.model_name))

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)


class PC(models.Model):

    model_name = models.CharField(max_length=64)
    cost = models.FloatField(null=True)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=120)
    image = models.ImageField(blank=True)


    class Meta:
        verbose_name = "PC"
        verbose_name_plural = "PC's"
        ordering = ['-date']

    def __str__(self):
        return ("{}".format(self.model_name))

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)

class Laptop(models.Model):
    name = models.CharField(max_length=64)
    cost = models.FloatField(null=True)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=120)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Laptop"
        verbose_name_plural = "Laptops"
        ordering = ['-date']

    def __str__(self):
        return ("{}".format(self.name))

    def get_absolute_url(self):
        return reverse("salesite:showDev", id=self.id)


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    servers = models.ManyToManyField(Server)
    laptops = models.ManyToManyField(Laptop)
    pcs = models.ManyToManyField(PC)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return ("{}".format(self.id + " " + self.customer))