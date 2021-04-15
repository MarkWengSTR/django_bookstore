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
    store_name = models.CharField(max_length=100, null =False)
    opening_hours = models.ManyToManyField('OpeningHours')


class Book(models.Model):
    books = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)

class OpeningHours(models.Model):
    week_day = models.CharField(max_length=20, choices=WEEKDAYS)
    start_min = models.TimeField()
    end_min = models.TimeField()
    


