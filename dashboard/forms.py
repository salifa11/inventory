from django import forms
from .models import Product
from .models import Category
from .models import Order

class ProductForm(forms.ModelForm):
   

    class Meta:
        model = Product
        fields =['name','category','size','condition','fabric','quantity','price']

class CategoryForm(forms.ModelForm):
   

    class Meta:
        model = Category
        fields =['name']

class OrderForm(forms.ModelForm):
   

    class Meta:
        model = Order
        fields =['product','category','user','order_quantity']