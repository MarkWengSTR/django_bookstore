from django.db import models

import bookstore_api.models as mods


class BookStoreManager(models.Manager):
    def list_store_open_at(self, req_hour, req_min):
        objs = mods.OpeningHour.objects.list_object_open_at(
            req_hour, req_min)

        return list(set(map(lambda obj: obj.book_store, objs)))

    def list_store_open_weekday_at(self, week_day, req_hour, req_min):
        objs = mods.OpeningHour.objects.list_object_open_at(
            req_hour, req_min)

        objs_in_weekday = filter(lambda obj: obj.week_day == week_day, objs)

        return list(set(map(lambda obj: obj.book_store, objs_in_weekday)))
