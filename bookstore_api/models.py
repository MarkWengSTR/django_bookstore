from django.db import models

# # Create your models here.


class BookStore(models.Model):
    cash_balance = models.FloatField(null=False)
    store_name = models.CharField(max_length=100, null=False)


class Book(models.Model):
    books_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)


class OpeningHour(models.Model):
    class WeekDay(models.TextChoices):
        MON = "Mon", "Monday"
        TUES = "Tues", "Tuesday"
        WED = "Wed", "Wednesday"
        THURS = "Thurs", "Thursday"
        FRI = "Fri", "Friday"
        SAT = "Sat", "Saturday"
        SUN = "Sun", "Sunday"

    books_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=5, choices=WeekDay.choices)
    start_hour = models.PositiveSmallIntegerField(null=True)
    start_min = models.PositiveSmallIntegerField(null=True)
    end_hour = models.PositiveSmallIntegerField(null=True)
    end_min = models.PositiveSmallIntegerField(null=True)
