from django.shortcuts import render
from .forms import LoginForm, RegForm
from django.http import HttpResponse


# Create your views here.
def index(request):
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


def regForm(request):
    if request.method == "POST":
        regF = RegForm(request.POST)
        if regF.is_valid():
            name = regF.cleaned_data["name"]
            last_name = regF.cleaned_data["last_name"]
            gender = regF.cleaned_data["gender"]
            birth  = regF.cleaned_data["birth"]
            firm  = regF.cleaned_data["firm"]
            phone = regF.cleaned_data["phone"]
            password = regF.cleaned_data["password"]
            return HttpResponse("{0} {1}!".format(name, last_name))
    else:
        Rform = RegForm()
        context = {"form": Rform}
        return render(request, "modalRegister.html", context)





