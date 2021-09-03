from django.db import models

from datetime import time
from bookstore_api.utils.time import time_in_range


class OpeningHourManager(models.Manager):
    def list_object_open_at(self, req_hour, req_min):
        req_hour, req_min = int(req_hour), int(req_min)
        return list(
            filter(lambda obj:
                   time_in_range(
                       time(obj.start_hour, obj.start_min),
                       time(obj.end_hour, obj.end_min),
                       time(req_hour, req_min)
                   ),
                   self.get_queryset().select_related('book_store')  # avoid double query
                   )
        )

    def find_more_or_less_open_hours(self, req_hours, compare='larger'):
        if compare == 'larger':
            return list(
                filter(lambda obj:
                       obj.open_hours() > req_hours,
                       self.get_queryset().select_related('book_store')
                       )
            )
        else:
            return list(
                filter(lambda obj:
                       obj.open_hours() < req_hours,
                       self.get_queryset().select_related('book_store')
                       )
            )
