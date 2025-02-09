from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    condition = models.CharField(max_length=50)
    fabric= models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
       return self.name
    

class Order(models.Model):

 product= models.ForeignKey(Product,on_delete=models.CASCADE)
 category=models.ForeignKey(Category,on_delete=models.CASCADE)
 user= models.ForeignKey(User,models.CASCADE,null=True)
 order_quantity=models.PositiveIntegerField()
 date=models.DateTimeField(auto_now_add=True)

       
 def __str__(self):
    return f'{self.product} order placed by {self.user}'
    