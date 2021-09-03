import json
import re
import os
from  datetime import datetime
from django.db import migrations

user_data_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../data'))
user_data_filename = 'user_data.json'


def parse_date_str(date_str):
    # pm convert to am , am still am 
    old_date = datetime.strptime(date_str, '%m/%d/%Y %I:%M %p')
    new_date = datetime.strftime(old_date, '%Y-%m-%d %H:%M')
    return datetime.strptime(new_date, '%Y-%m-%d %H:%M')

def load_user_data(apps, shema_editor):
    user_data_file = os.path.abspath(
            os.path.join(user_data_dir, user_data_filename))
    with open(user_data_file, 'r') as user_data:
        data = json.load(user_data)
        User = apps.get_model("bookstore_api", "User")
        PurchaseHistory = apps.get_model("bookstore_api", "PurchaseHistory")

        for store_data in data:
           us = User(
               cash_balance=store_data['cashBalance'],
               id = store_data['id'],
               name=store_data['name'],
            )
           us.save()

           for purchase in store_data['purchaseHistory']:
#              import ipdb
#              ipdb.set_trace()
              PurchaseHistory(
                 user=us,
                 book_name=purchase['bookName'],
                 store_name=purchase['storeName'],
                 transaction_amount=purchase['transactionAmount'],
                 transaction_date=parse_date_str(purchase['transactionDate']),

             ).save()

def unload_user_data(apps, schema_editor):
    User = apps.get_model("bookstore_api", "User")
    PurchaseHistory = apps.get_model(
        "bookstore_api", "PurchaseHistory")
    for mod in [User, PurchaseHistory]:
        mod.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('bookstore_api','0004_auto_20210420_0917'),
    ]

    operations = [
        migrations.RunPython(load_user_data, reverse_code = unload_user_data),
    ]
