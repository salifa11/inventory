from django.urls import path
from . import views

urlpatterns =[

path ('', views.index, name='dashboard-index'),
path('category/',views.category,name='dashboard-category')
]