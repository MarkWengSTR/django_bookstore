from django.db import models
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

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
            result = filter(lambda store:
                            store.weekly_open_hours() > req_hours,
                            stores)
        else:
            result = filter(lambda store:
                            store.weekly_open_hours() < req_hours,
                            stores)
        return list(result)

    def list_compared_books_num(self, req_num, compare):
        req_num = int(req_num)
        stores = self.get_queryset().prefetch_related('book_set')

        if compare == 'larger':
            result = filter(lambda store:
                            store.book_set.all().count() > req_num,
                            stores)
        else:
            result = filter(lambda store:
                            store.book_set.all().count() < req_num,
                            stores)
        return list(result)

    def list_compared_books_num_price_range(self, req_num, compare, req_low_price, req_high_price):
        return list(
            filter(lambda store:
                   store.book_set.filter(
                       price__gt=req_low_price, price__lt=req_high_price),
                   self.list_compared_books_num(req_num, compare)))

    def list_search_by_name(self, req_name):
        vector = SearchVector('name')
        query = SearchQuery(req_name)

        return self.annotate(rank=SearchRank(vector, query)).order_by('-rank')
