from django.urls import path
from . import views


urlpatterns =[

path ('dashboard/', views.index, name='dashboard-index'),
path('category/',views.category,name='dashboard-category'),
path('product/',views.product,name='dashboard-product'),
path('order/',views.order,name='dashboard-order'),
path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
path('order/delete/<int:pk>/',views.order_delete,name='dashboard-order-delete'),
path('order/update/<int:pk>/',views.order_update,name='dashboard-order-update'),
path('category/delete/<int:pk>/',views.category_delete,name='dashboard-category-delete'),
path('category/update/<int:pk>/',views.category_update,name='dashboard-category-update'),
]