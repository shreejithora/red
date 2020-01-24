from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return render(requests, 'index.html')

def donateview(requests):
    return render(requests, 'donate.html')

def donateform(requests):
    return HttpResponse('this is donateform')
