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

    def list_compared_open_hours_per_weekday(self, week_day, req_hours, compare):
        req_hours = int(req_hours)

        objs = mods.OpeningHour.objects.find_more_or_less_open_hours(
            req_hours, compare)

        objs_in_weekday = filter(lambda obj: obj.week_day == week_day, objs)

        return list(set(map(lambda obj: obj.book_store, objs_in_weekday)))

    def list_compared_open_hours_per_week(self, req_hours, compare):
        req_hours = int(req_hours)
        stores = self.get_queryset().prefetch_related('openinghour_set')

        if compare == 'larger':
            return list(
                filter(lambda store:
                       store.weekly_open_hours() > req_hours,
                       stores
                       )
            )
        else:
            return list(
                filter(lambda store:
                       store.weekly_open_hours() < req_hours,
                       stores
                       )
            )
