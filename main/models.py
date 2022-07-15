from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    products = models.ManyToManyField(Product, through='OrderItems')

    def __str__(self):
        return f'Order #{self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField()
