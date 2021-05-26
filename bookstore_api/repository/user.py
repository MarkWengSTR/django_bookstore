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

    def list_date_range_user_total(self, req_amount, req_compare, req_low_date, req_high_date):
        from bookstore_api.models import User

        req_amount = int(req_amount)

        # user_amount_compare_amount
        if req_compare == 'larger':
            username_and_amount_in_date_range = User.objects.filter(
                purchasehistory__transaction_date__range=[
                    req_low_date, req_high_date], purchasehistory__transaction_amount__gte=req_amount
            ).values('name', 'purchasehistory__transaction_amount').order_by('name')

        else:
            username_and_amount_in_date_range = User.objects.filter(
                purchasehistory__transaction_date__range=[
                    req_low_date, req_high_date], purchasehistory__transaction_amount__lte=req_amount
            ).values('name', 'purchasehistory__transaction_amount').order_by('name')

        user_count = {"user_count": username_and_amount_in_date_range.distinct('name').count()}
        user_amount = {"user_amount": username_and_amount_in_date_range}

        return {**user_count, **user_amount}
