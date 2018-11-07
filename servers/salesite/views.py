from django.shortcuts import render
from .forms import LoginForm, RForm
from django.http import HttpResponse
from salesite.models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404


# Create your views here.
class Index(View):

    def get(self, request):
        logForm = LoginForm()
        return render(request, 'index.html', context={'form': logForm})

    def post(self, request):
        lf = LoginForm(request.POST)
        if lf.is_valid():
            log = lf.cleaned_data["login"]
            return HttpResponse("<h1>Hello {}!</h1>".format(log))
        else:
            return HttpResponse("<h1>Invalid data!</h1>")




class RegForm(View):

   def get(self, request):
        regForm = RForm()
        return render(request, 'modalRegister.html', context={'regForm': regForm})

   def post(self, request):
       regF = RegForm(request.POST)
       if regF.is_valid():
           name = regF.cleaned_data["name"]
           last_name = regF.cleaned_data["last_name"]
           gender = regF.cleaned_data["gender"]
           birth = regF.cleaned_data["birth"]
           firm = regF.cleaned_data["firm"]
           phone = regF.cleaned_data["phone"]
           password = regF.cleaned_data["password"]
           return HttpResponse(name + " "  + last_name + " was registered." )


class PricesTemplate(View):

    def get(self, request):
        return render(request, "prices_template.html")


class PricesLaptop(View):

    def get(self, request):
        laptops = Laptop.objects.all()
        return render(request, "prices_devices.html", context={"devices": laptops})



class Fedback(View):

    def get(self, request):
        return render(request, "fedback.html")



class ShowDew(View):

    def get(self, request):
        return HttpResponse(request, "<h1>It works!")



