from django.db import models
from django.contrib.auth.models import AbstractUser

# Normal models.

# class Users(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True, blank=False)
#     contactNo = models.CharField(max_length=10)
#     dob = models.DateField()
#     address = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.id)


# Abstract User
class Users(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    contactNo = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    username = None
    password = models.CharField(default='password', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)
