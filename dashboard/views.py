from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from .models import Category
from .forms import CategoryForm
from .models import Order
from .forms import OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='user-login')
def index(request):
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    users = User.objects.all()
    user_count = users.count()
    total_price =0

    for item in orders:
        total_price += item.product.price * item.order_quantity
    context ={
        'product_count': product_count,
        'order_count' : order_count,
        'user_count' : user_count,
        'orders' : orders,
        'total_price' :total_price
    }
    return render(request,'dashboard/index.html',context)
    

# ----------------- CATEGORY VIEWS -----------------
@login_required(login_url='user-login')
def category(request):
    items = Category.objects.all() # Fetch all Category objects from the database
    if request.method == 'POST':  # Check if the request is a form submission
        form = CategoryForm(request.POST) # Create a form instance with submitted data
        if form.is_valid():
            form.save()  # Save the new category to the database
            category_name = form.cleaned_data.get('name')   # Get the category name (optional)
        messages.success(request, f'{category_name} added successfully ')
        return redirect('dashboard-category')
    else:
        form = CategoryForm() 
    
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/category.html', context)


@login_required(login_url='user-login')
def category_delete(request, pk):
    item = Category.objects.get(id=pk) #Fetches a single Category object where the id matches pk (primary key).
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-category')
    return render(request,'dashboard/category_delete.html')


def category_update(request, pk):
    item = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('dashboard-category')
    else:
         form = CategoryForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request,'dashboard/category_update.html',context)





# ----------------- ORDER VIEWS -----------------
@login_required(login_url='user-login')
def order(request):
    items = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        order_name = form.cleaned_data.get('product')
        messages.success(request, f'{order_name} added successfully ')
        return redirect('dashboard-order')
    else:
        form = OrderForm() 
    
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/order.html', context)




@login_required(login_url='user-login')
def order_delete(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-order')
    return render(request,'dashboard/order_delete.html')

def order_update(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('dashboard-order')
    else:
         form = OrderForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request,'dashboard/order_update.html',context)


    


# ----------------- PRODUCT VIEWS -----------------
@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            #flash message work
        product_name = form.cleaned_data.get('name')
        messages.success(request, f'{product_name} added successfully ')
        return redirect('dashboard-product')
    else:

        form = ProductForm() 
      
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/product.html',context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('dashboard-product')
    else:
         form = ProductForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request,'dashboard/product_update.html',context)

