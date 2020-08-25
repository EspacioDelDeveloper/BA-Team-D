from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("este es el home")


def about(request):
    return HttpResponse("sobre nosotros")


def contact(request):
    return HttpResponse("comunicate con nosotros")

