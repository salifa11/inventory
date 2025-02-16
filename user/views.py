from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('user-login')
    else:
      form = CreateUserForm() 

    context = {

        'form' : form,
    }
    return render(request,'user/register.html',context)

@login_required(login_url='user-login')
def Profile(request):
   return render(request,'user/profile.html')