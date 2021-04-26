from django.db import models
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


class BookManager(models.Manager):
    def list_book_by_price(self, req_low_price, req_high_price, sort='name'):
        return self.filter(price__gt=req_low_price, price__lt=req_high_price).order_by("-" + sort)

    def list_search_by_name(self, req_name):
        vector = SearchVector('name')
        query = SearchQuery(req_name)

        return self.annotate(rank=SearchRank(vector, query)).order_by('-rank')
