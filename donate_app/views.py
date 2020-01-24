from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import *
# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'index.html'

def home(requests):
    return render(requests, 'index.html')

def donateview(requests):
    return render(requests, 'Donate.html')

def donateform(requests):
    return render(requests, 'donation_form.html')
