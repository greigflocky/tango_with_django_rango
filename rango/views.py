from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!" "<p><a href='/rango/about/'>About</a></p>")

def about(request):
    return HttpResponse("Rango says here is the about page." "<p><a href='/rango/'>Index</a></p>")
