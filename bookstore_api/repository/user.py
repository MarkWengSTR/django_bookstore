from django.db import models


class UserManager(models.Manager):
    def list_user_date_range_amount(self, req_num, req_low_date, req_high_date):
        from bookstore_api.models import User
        from django.db.models import Sum

        # user_date_range_amount
        req_num = int(req_num)
        user_date_range_amount = User.objects.values('name') \
            .filter(purchasehistory__transaction_date__range=[req_low_date, req_high_date]) \
            .annotate(Sum('purchasehistory__transaction_amount'))

        # sort user_amount_limit
        user_amount_limit = user_date_range_amount.order_by('-purchasehistory__transaction_amount__sum')[:req_num]

        return list(user_amount_limit)
