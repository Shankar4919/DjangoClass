from django.db import models
from django.core import validators
from django.core.validators import *


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=200,null=True, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(unique=True, null=True, validators=[validate_email])
    phone = models.CharField(max_length=10, null=True, validators=[validators.MinLengthValidator(9)])

    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    batch = models.IntegerField(null=True)
    image_url = models.CharField(max_length=2000, null=True)
    category = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.firstname


class FileUpload(models.Model):
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='static/uploads')