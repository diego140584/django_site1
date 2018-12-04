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

        laptop = Laptop.objects.all()
        paginator = Paginator(laptop, 8)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        has_pages = page.has_other_pages()
        if page.has_previous():
            prew_page = '?page={}'.format(page.previous_page_number())
        else:
            prew_page = ''

        if page.has_next():
            next_page = '?page={}'.format(page.next_page_number())
        else:
            next_page = ''

        pages = {
            'page': page,
            'has': has_pages,
            'preview': prew_page,
            'next': next_page
        }

        return render(request, "prices_devices.html", context=pages)

class PricesPC(View):
    def get(self, request):
        pc = PC.objects.all()
        paginator = Paginator(pc, 3)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request,'prices_devices.html', context={'devices': page})


class PricesServer(View):
    def get(self, request):
        server = Server.objects.all()
        paginator = Paginator(server, 3)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request,'prices_devices.html', context={'devices': page})



class Fedback(View):

    def get(self, request):
        return render(request, "fedback.html")



class ShowDew(View):

    def get(self, request):
        return HttpResponse(request, "<h1>It works!")



