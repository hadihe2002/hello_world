from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("<center>Hello World<center>")
# Create your views here.
