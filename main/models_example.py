from django.db import models

#Один ко многим
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, primary_key=True)

# category1 = Category(...)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

# p1 = Product(..., category=category1)
# p2 = Product(..., category=category1)


class Author(models.Model):
    name = models.CharField(...)
    last_name = models.CharField(...)
    date_of_birth = models.DateField(...)

# author1 = Author('Иван', 'Тургенев')

# author1.books.all()

class Book(models.Model):
    name = models.CharField(...)
    year = models.IntegerField(...)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='books')


# book1 = Book('Муму', ..., author=author1)
# CASCADE, RESTRICT, SET_NULL, SET_DEFAULT

class Employee(models.Model):
    name = models.CharField(...)
    last_name = models.CharField(...)
    date_of_birth = models.DateField(...)
    ...
    chief = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subordinates', null=True, blank=True)

#Один к одному

class Citizen(models.Model):
    name = models.CharField(...)
    last_name = models.CharField(...)
    date_of_birth = models.DateField(...)
    country = models.ForeignKey(Country, null=True, blank=True)


# p1 = Citizen('Vladimir', 'Putin', '...')
citizen1 = Citizen('Илья', 'Маховский', '25.09.1991', country1 )

citizen1.country.president
# p1.country.square

class Country(models.Model):
    name = ...
    population = ...
    square = ...
    president = models.OneToOneField(Citizen, on_delete=models.CASCADE)

country1 = Country('Russian Federation', 150000000, ..., p1)

#Много ко многих
class Student(models.Model):
    name = models.CharField(...)
    last_name = models.CharField(...)
    date_of_birth = models.DateField(...)


class Course(models.Model):
    name = ...
    description = ...
    duration = ...
    cost = ...
    students = models.ManyToManyField(Student)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Purchase(models.Model):
    customer = ...
    date = ...
    cost = ...
    address = ...
    products = models.ManyToManyField(Product, through='PurchaseItems')


class PurchaseItems(models.Model):
    purchase = models.ForeignKey(Purchase,...)
    product = models.ForeignKey(Product, ...)
    quantity = models.IntegerField()