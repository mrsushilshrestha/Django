from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("Hello")

def login(request):
    return HttpResponse("HI")