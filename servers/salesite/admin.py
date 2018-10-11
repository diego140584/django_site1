from django.contrib import admin
from salesite.models import Customer, Order, Server, PC, Laptop

# Register your models here.

admin.site.register(Customer)
admin.site.register(Server)
admin.site.register(PC)
admin.site.register(Laptop)
admin.site.register(Order)



