from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_app.models import UserModel
from user_app.forms import UserForm

# Create your views here.

def signupform(request):
    form = UserForm()
    context={'form':form}
    return render(request, 'signup.html', context)

def signup(request):

      if(request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate_app:donateform')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid') 

def loginauth(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('pass')
        users = UserModel.objects.filter(email=e, password=p)
        if(users.count() > 0):
            for user in users:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['name'] = user.name
                return redirect('home')
        else:
            return HttpResponse('Wrong Credentials')
    else:
        return render(request, 'login.html')
