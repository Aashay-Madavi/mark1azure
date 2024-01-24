from django.db import models
from products.models import Products
from users.models import Users
# Create your models here.


status = (
    ("pending", "Pending"),
    ("cancled", "Cancled"),
    ("delivered", "Delivered")
)


class Orders(models.Model):
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        default='pending', choices=status, max_length=100)
    quantity = models.IntegerField(default=1)
