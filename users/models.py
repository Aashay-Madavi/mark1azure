from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .manager import UserManager

# Normal models.

# class Users(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True, blank=False)
#     contact_no = models.CharField(max_length=10)
#     dob = models.DateField()
#     address = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.id)


# Abstract User
class Users(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    contactNo = models.CharField(max_length=10, unique=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)
