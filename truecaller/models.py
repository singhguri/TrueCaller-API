from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    phnNumber = PhoneNumberField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, blank=True, default="")
    isSpam = models.BooleanField(default=False)
    isRegistered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Spam(models.Model):
    user_id = models.AutoField(primary_key=True)
    phnNumber = PhoneNumberField(unique=True, null=False)
    email = models.EmailField(max_length=254, blank=True, default="")
    isSpam = models.BooleanField(default=False)

    def __str__(self):
        return self.phnNumber
