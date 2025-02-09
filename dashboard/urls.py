from django.urls import path
from . import views

urlpatterns =[

path ('', views.index, name='dashboard-index'),
path('category/',views.category,name='dashboard-category'),
path('product/',views.product,name='dashboard-product'),
path('Account/',views.orders,name='dashboard-Account'),
]