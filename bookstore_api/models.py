from django.db import models

WEEKDAYS = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
        (4, ("Thursday")),
        (5, ("Friday")),
        (6, ("Saturday")),
        (7, ("Sunday")),
]
# Create your models here.
class Bookstore(models.Model):
    cashBalance = models.FloatField(null=False)
    books = models.ForeignKey('Book', on_delete=models.CASCADE)
    openingHours = models.ManyToManyField('OpeningHours')
    storeName = models.CharField(max_length=100, null =False)

class Book(models.Model):
    bookname = models.CharField(max_length=100, null=False)
    price = FloatField(null=Fasle)

class OpeningHours(models.Model):
    weekay = models.CharField(max_length=20, choices=WEEKDAYS)
    start_min = models.IntegerField(null = False)
    end_min = models.IntegerField(null = False)
    


