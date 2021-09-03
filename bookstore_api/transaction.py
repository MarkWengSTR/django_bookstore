from .models import User, BookStore, Book, PurchaseHistory
from django.db import transaction
from datetime import datetime

@transaction.atomic
def User_Purchase(user, book):
    user = User.objects.get(name=user)
    bookstore = BookStore.objects.get(book__name=book)
    book = Book.objects.get(name=book)

    try:
        with transaction.atomic():
            if (user.cash_balance - book.price) > 0:
                user.cash_balance -= book.price
                bookstore.cash_balance += book.price
                
                User.objects.select_for_update().filter(name=user.name)\
                        .update(cash_balance = user.cash_balance)
                User.objects.get(name=user.name).purchasehistory.create(\
                        book_name = book.name,
                        store_name = bookstore.name,
                        transaction_amount = book.price,
                        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        )
                BookStore.objects.filter(book__name=book.name).update(
                        cash_balance = bookstore.cash_balance)

    except User.DoesNotExist:
        return False

