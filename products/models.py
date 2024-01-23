from django.db import models

# Create your models here.


Product_Category = (
    ("electronics", "electronics"),
    ("books", "Books"),
    ("watches", "Watches")
)


class Products(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField(max_length=1000)
    category = models.CharField(max_length=100, choices=Product_Category)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
