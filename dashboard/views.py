from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='user-login')
def index(request):
    return render(request,'dashboard/index.html')

@login_required(login_url='user-login')
def category(request):
   return render(request,'dashboard/category.html')

@login_required(login_url='user-login')
def product(request):
    return render(request,'dashboard/product.html')

@login_required(login_url='user-login')
def orders(request):
    return render(request,'dashboard/Account.html')
    
