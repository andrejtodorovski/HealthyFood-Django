from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)


class Product(models.Model):
    code = models.CharField(max_length=10, auto_created=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")
    price = models.IntegerField()
    quantity = models.IntegerField()
    objects = models.Manager()  # Add the objects attribute explicitly

    def __str__(self):
        return self.name


class ProductIsInTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name + " " + str(self.quantity)
