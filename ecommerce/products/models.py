from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=200, null=True)

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