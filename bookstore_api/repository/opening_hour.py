from django.db import models

from datetime import time
from bookstore_api.utils.time import time_in_range


class OpeningHourManager(models.Manager):
    def list_object_open_at(self, req_hour, req_min):
        req_hour, req_min = int(req_hour), int(req_min)
        return list(
            filter(lambda data:
                   time_in_range(
                       time(data.start_hour, data.start_min),
                       time(data.end_hour, data.end_min),
                       time(req_hour, req_min)
                   ),
                   self.get_queryset()
                   )
        )

    def list_store_open_at(self, req_hour, req_min):
        objs = self.list_object_open_at(req_hour, req_min)

        return list(set(map(lambda obj: obj.book_store, objs)))

    def list_store_open_weekday_at(self, week_day, req_hour, req_min):
        objs = self.list_object_open_at(req_hour, req_min)

        objs_in_weekday = filter(lambda obj: obj.week_day == week_day, objs)

        return list(set(map(lambda obj: obj.book_store, objs_in_weekday)))
