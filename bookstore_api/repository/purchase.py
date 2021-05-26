from django.db import models

class PurchaseManager(models.Manager):
    def list_purchase_count_amount(self, req_low_date, req_high_date):
        from bookstore_api.models import PurchaseHistory
        from django.db.models import Sum, Count

        date_range_pur_amount = PurchaseHistory.objects \
                                .filter(transaction_date__range=[req_low_date, req_high_date]) \
                                .aggregate(Sum('transaction_amount'))

        date_range_pur_count = PurchaseHistory.objects.filter(transaction_date__range=[req_low_date, req_high_date]).aggregate(Count('transaction_amount'))
        
        return {**date_range_pur_count , **date_range_pur_amount}
