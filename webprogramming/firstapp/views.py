from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("First project using Django")
def about(request):
    return HttpResponse("<h2>About</h2>")
def contact(request):
    return HttpResponse("<h2>Contact</h2>")
def product(request, productId = 1):
    return HttpResponse("<h2>Contact {0} </h2>".format(productId))
def user(request, id, name):
    return HttpResponse("<h2>User {0} {1}</h2>".format(id, name))