from django.shortcuts import render
from .forms import LoginForm, RForm
from django.http import HttpResponse
from salesite.models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


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
       regF = RForm(request.POST)
       if regF.is_valid():
           regF.save()
           return redirect(regF)
       else:
           return render(request, 'modalRegister.html', context={'regForm': regF})


class PricesTemplate(View):

    def get(self, request):
        return render(request, "prices_template.html")


class PricesLaptop(View):

    def get(self, request):
        paginator = Paginator(Laptop, 3)
        page = paginator.get_page(1)
        laptops = Laptop.objects.all()
        return render(request, "prices_devices.html", context={"devices": page.object_list})



class Fedback(View):

    def get(self, request):
        return render(request, "fedback.html")



class ShowDew(View):

    def get(self, request):
        return HttpResponse(request, "<h1>It works!")



