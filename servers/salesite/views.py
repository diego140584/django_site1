from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse,request


# Create your views here.
def index(request):
    if request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            login = lf.cleaned_data("login")
            return HttpResponse("<h1>Hello {}!</h1>".format(login))

        else:
            return HttpResponse("<h1>Invalid data!</h1>")
    else:
        logform = LoginForm()
        context = {"form": logform}
        return render(request, 'index.html', context)



