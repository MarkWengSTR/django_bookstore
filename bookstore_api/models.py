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
class BookStore(models.Model):
    cash_balance = models.FloatField(null=False)
    books = models.ForeignKey('Book', on_delete=models.CASCADE)
    opening_hours = models.ManyToManyField('OpeningHours')
    store_name = models.CharField(max_length=100, null =False)

class Book(models.Model):
    book_name = models.CharField(max_length=100, null=False)
    price = FloatField(null=Fasle)

class OpeningHours(models.Model):
    week_day = models.CharField(max_length=20, choices=WEEKDAYS)
    start_min = models.TimeField()
    end_min = models.TimeField()
    


