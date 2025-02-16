from django.urls import path
from . import views


urlpatterns =[

path ('dashboard/', views.index, name='dashboard-index'),
path('category/',views.category,name='dashboard-category'),
path('product/',views.product,name='dashboard-product'),
path('Account/',views.orders,name='dashboard-Account'),
path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
]