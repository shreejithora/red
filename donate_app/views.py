from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DonateForm
from django.views.generic import *

# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'index.html'

def home(requests):
    return render(requests, 'index.html')

# def donateview(requests):
#     return render(requests, 'Donate.html')

def donateform(requests):
    form = DonateForm()
    context = {'form' : form}
    return render(requests, 'donation_form.html', context)

def adddonation(request):
    if(request.method == 'POST'):
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate_app:home')
            # try:
            # except:
            #     return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid')
    else:
        # form = QuestionForm
        datecategory = DateCategoryModel.objects.all()
        return render(request, 'questionmodel_create.html', {'datecategory':datecategory})

def team(request):
    return render(request, 'team.html')

