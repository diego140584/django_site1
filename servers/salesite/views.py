from django.shortcuts import render
from .forms import LoginForm


# Create your views here.
def index(request):
    logform = LoginForm()
    context = {"form": logform}

    return render(request, 'index.html', context)


