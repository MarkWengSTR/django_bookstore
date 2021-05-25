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


    def list_date_range_user_total(self,req_amount, req_compare, req_low_date, req_high_date):
        from bookstore_api.models import User

        req_amount = int(req_amount) 

        # user_amount_compare_amount
        if req_compare == 'larger':
            date_range_user_amount = User.objects.filter(
                    purchasehistory__transaction_date__range=[
                    req_low_date, req_high_date], purchasehistory__transaction_amount__gte = req_amount
                    ).values('name','purchasehistory__transaction_amount')

        else:
            date_range_user_amount = User.objects.filter(
                    purchasehistory__transaction_date__range=[
                    req_low_date, req_high_date], purchasehistory__transaction_amount__lte = req_amount
                    ).values('name','purchasehistory__transaction_amount')

        # user_count_distinct
        date_range_user_count = date_range_user_amount.distinct('name').count()

        # return {"user_count":  ,"purchase":[]}
        date_range_user_amount = list(map(lambda amount: amount, \
                    date_range_user_amount.order_by('name').distinct()
                                        )
                    )

        user_count = {"user_count": date_range_user_count}
        user_amount = {"user_amount": date_range_user_amount}

        return {**user_count, **user_amount}
