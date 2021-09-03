from django.db import models
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


class BookManager(models.Manager):
    def list_book_by_price(self, req_low_price, req_high_price, sort='name'):
        req_low_price, req_high_price = \
            int(req_low_price), int(req_high_price)

        sort = 'name' if sort not in ['name', 'price'] else sort

        return self.filter(price__gt=req_low_price, price__lt=req_high_price).order_by("-" + sort)

    def list_search_by_name(self, req_name):
        vector = SearchVector('name')
        query = SearchQuery(req_name)

        return self.annotate(rank=SearchRank(vector, query)).order_by('-rank')
