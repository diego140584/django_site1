from django.shortcuts import render
from .forms import LoginForm, RegForm
from django.http import HttpResponse
from salesite.models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404


# Create your views here.
class Index(View):
    def get(self, request):
        if request.method == "POST":
            lf = LoginForm(request.POST)
            if lf.is_valid():
                log = lf.cleaned_data["login"]
                return HttpResponse("<h1>Hello {}!</h1>".format(log))

            else:
                return HttpResponse("<h1>Invalid data!</h1>")
        else:
            logform = LoginForm()
            context = {"form": logform}
            return render(request, 'index.html', context)


class RegForm(View):
    def get(self, request):
        def regForm(request):
            if request.method == "POST":
                regF = RegForm(request.POST)
                if regF.is_valid():
                    name = regF.cleaned_data["name"]
                    last_name = regF.cleaned_data["last_name"]
                    gender = regF.cleaned_data["gender"]
                    birth = regF.cleaned_data["birth"]
                    firm = regF.cleaned_data["firm"]
                    phone = regF.cleaned_data["phone"]
                    password = regF.cleaned_data["password"]
                    return HttpResponse("")
            else:
                Rform = RegForm()
                context = {"form": Rform}
                return render(request, "modalRegister.html", context)


class Prices(View):
    def get(self, request):
        laptops = Laptop.objects.all()

        return render(request, "prices.html", context={"devices": laptops})



def fedback(request):
    return render(request, "fedback.html")


#def showDev(request):
#   return HttpResponse("<h1>It works!")


class ShowDew(View):
    def get(self, request):
        return HttpResponse(request, "<h1>It works!")



