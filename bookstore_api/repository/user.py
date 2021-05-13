from django.db import models
from django.contrib.postgres.search import SearchQuery,SearchRank, SearchVector

class UserManager(models.Manager):
    def list_user_amount_date_range(self, req_num, req_amount, req_low_date, req_high_date):
        from bookstroe_api.models import PurchaseHistory
        from bookstroe_api.models import Sum
        users = self.get_queryset()
        # date range
        PurchaseHistory.objects.filter(transaction_date__gte= req_low_date)
        PurchaseHistory.objects.filter(transaction_date__gte= req_low_date).aggregate(Sum('transaction_amount'))
        # total amount
        return list(
                filter(lambda use:
                       user._set.filter(
                                                       transaction_date__lte= req_high_date
                        )
                    )
                )
