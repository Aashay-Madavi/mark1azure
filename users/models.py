from django.db import models


# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    contactNo = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
