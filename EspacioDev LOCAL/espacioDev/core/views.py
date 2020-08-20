from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("este es el home")


def about(request):
    return HttpResponse("sobre nosotros")


def portfolio(request):
    return HttpResponse("este es nuestro portfolio")


def contact(request):
    return HttpResponse("nuestros medios de comunicación")


def blog(request):
    return HttpResponse("nuestro blog")

