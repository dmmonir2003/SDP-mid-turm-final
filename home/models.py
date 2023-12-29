from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CarBrand(models.Model):
     brand_name=models.CharField(max_length=100)
     quantity=models.PositiveIntegerField(default=0)
     slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

     def __str__(self):
         return self.brand_name
     

class Car(models.Model):
    brand=models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    car_image=models.ImageField(upload_to='car_images/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    car_quantity=models.PositiveIntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True) 
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.user.username} - {self.car.name}-{self.car.car_image}"


class Comment(models.Model):
    car_comments = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments',blank=True,default=None,null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    