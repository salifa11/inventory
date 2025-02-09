from django.contrib import admin
from . models import Category
from . models import Product,Order


admin.site.site_header='Thrift Admin'

class ProductAdmin(admin.ModelAdmin): 
      list_display=('name','category','condition','price')
      list_filter=['category']


# Register your models here.

admin.site.register(Category)

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)

#to display desired data

