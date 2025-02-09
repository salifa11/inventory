from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'dashboard/index.html')
    
def category(request):
   return render(request,'dashboard/category.html')

def product(request):
    return render(request,'dashboard/product.html')

def orders(request):
    return render(request,'dashboard/Account.html')
    
