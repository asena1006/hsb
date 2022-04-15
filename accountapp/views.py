from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')


class AccountCreateView(CreateView):
    model = User