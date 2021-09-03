from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from bookstore_api.utils.time import add_12_afternoon
from bookstore_api.models import BookStore, Book, User, PurchaseHistory
from bookstore_api.decorators.request import req_keys_check, req_params_in_key_check
from bookstore_api.serializers.serializer import UpdateSerializer
from bookstore_api.transaction import User_Purchase
from django.db import transaction
from datetime import datetime
import json
# Create your views here.


@swagger_auto_schema(methods=['get'], operation_summary="GET Hello")
@api_view(['GET'])
def show_index(request):
    return Response({
        "msg": "Hello!",
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List book stores open at a certain datetime"
        )
@api_view(['GET'])
@req_keys_check(keys=["hour", "min", "noon"])
@req_params_in_key_check(params={"noon": ["am", "pm"]})
def find_store_open_at(request):
    """
    {
        hour: 2,
        min: 30,
        noon: pm
    }
    """
    req_hour = add_12_afternoon(
        request.query_params.get('hour'),
        request.query_params.get('noon')
    )
    req_min = request.query_params.get('min')

    open_stores_name = list(
        map(
            lambda store_obj: store_obj.name,
            BookStore.objects.list_store_open_at(req_hour, req_min)
        ))

    return Response({
        "open_stores": open_stores_name,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List all book stores open on a day of the week, \
        at a certain datetime"
        )
@api_view(['GET'])
@req_keys_check(keys=["hour", "min", "noon", "weekday"])
@req_params_in_key_check(params={
    "noon": ["am", "pm"],
    "weekday": ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
})
def find_store_open_weekday_at(request):
    """
    {
        hour: 2,
        min: 30,
        noon: pm,
        weekday: 'Wed'
    }
    """
    req_weekday = request.query_params.get('weekday')
    req_hour = add_12_afternoon(
        request.query_params.get('hour'),
        request.query_params.get('noon')
    )
    req_min = request.query_params.get('min')

    open_stores_name = list(
        map(
            lambda store_obj: store_obj.name,
            BookStore.objects.list_store_open_weekday_at(
                req_weekday, req_hour, req_min)
        ))

    return Response({
        "open_stores": open_stores_name,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List all book stores for more or less than x hours \
        per day or week"
        )
@api_view(['GET'])
@req_keys_check(keys=["weekday", "hours", "compare"])
@req_params_in_key_check(params={"compare": ["larger", "smaller"]})
def find_store_with_open_hour(request):
    """
    {
        weekday: 'Mon',
        hours: 40,
        compare: larger,
    }
    """
    req_weekday = request.query_params.get('weekday', '')
    req_hours = request.query_params.get('hours')
    req_compare = request.query_params.get('compare')

    if req_weekday == '':
        result_stores = map(
            lambda store_obj: store_obj.name,
            BookStore.objects.list_compared_open_hours_per_week(
                req_hours, req_compare)
        )
    else:
        result_stores = map(
            lambda store_obj: store_obj.name,
            BookStore.objects.list_compared_open_hours_per_weekday(
                req_weekday, req_hours, req_compare)
        )

    return Response({
        "open_stores": list(result_stores),
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List all books that are within a price range,\
        sorted by price or alphabetically" 
        )
@api_view(['GET'])
@req_keys_check(keys=["low_price", "high_price", "sort"])
@req_params_in_key_check(params={"sort": ["name", "price"]})
def find_books_in_price_range(request):
    """
    {
        low_price: 10,
        high_price: 30,
        sort: "name" or "price",
    }
    """
    req_low_price = request.query_params.get('low_price')
    req_high_price = request.query_params.get('high_price')
    req_sort = request.query_params.get('sort')

    result = list(
        map(
            lambda book: book.name,
            Book.objects.list_book_by_price(
                req_low_price, req_high_price, req_sort)
        )
    )

    return Response({
        "books": result,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List all book stores that have more or less \
        than x number of books"
        )
@api_view(['GET'])
@req_keys_check(keys=["num", "compare"])
@req_params_in_key_check(params={"compare": ["larger", "smaller"]})
def find_bookstore_have_num_of_books(request):
    """
    {
        num: 10,
        compare: larger,
    }
    """
    req_num = request.query_params.get('num')
    req_compare = request.query_params.get('compare')

    result = list(
        map(
            lambda store: store.name,
            BookStore.objects.list_compared_books_num(req_num, req_compare)
        )
    )

    return Response({
        "store": result,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary= "List all book stores that have more or less \
        than x number of books within a price range"
        )
@api_view(['GET'])
@req_keys_check(keys=["name", "compare", "low_price", "high_price"])
@req_params_in_key_check(params={"compare": ["larger", "smaller"]})
def find_bs_have_num_of_books_price_range(request):
    """
    {
        num: 10,
        compare: larger,
        low_price: 10,
        high_price: 30,
    }
    """
    req_num = request.query_params.get('num')
    req_compare = request.query_params.get('compare')
    req_low_price = request.query_params.get('low_price')
    req_high_price = request.query_params.get('high_price')

    result = list(
        map(
            lambda store: store.name,
            BookStore.objects.list_compared_books_num_price_range(
                req_num, req_compare, req_low_price, req_high_price)
        )
    )

    return Response({
        "store": result,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="Search for book stores or books by name, ranked by relevance to search term"
        )
@api_view(['GET'])
@req_keys_check(keys=["name", "book_or_store"])
@req_params_in_key_check(params={"book_or_store": ["book", "store"]})
def search_b_bs_by_name(request):
    """
    {
        name: Rails,
        book_or_store: book(or store),
    }
    """
    req_name = request.query_params.get('name')
    req_b_or_bs = request.query_params.get('book_or_store')

    if req_b_or_bs == 'store':
        result = map(
            lambda store: store.name,
            BookStore.objects.list_search_by_name(req_name)
        )
    else:
        result = map(
            lambda book: book.name,
            Book.objects.list_search_by_name(req_name)
        )

    return Response({
        req_b_or_bs: list(result),
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List The top x users by total transaction amount within a date range"
        )
@api_view(['GET'])
@req_keys_check(keys=["num", "low_date", "high_date"])
def find_user_date_range_amount(request):
    """
    {
        num: 10,
        low_date:"2021-03-10",
        high_date: "2021-04-03",
    }
    """
    req_num = request.query_params.get('num')
    req_low_date = request.query_params.get('low_date')
    req_high_date = request.query_params.get('high_date')

    result = list(map(lambda user: user, 
            User.objects.list_user_date_range_amount(
                req_num, req_low_date, req_high_date)
                     )
            )

    return Response({
        "user": result,
        "request_data": request.query_params
    })


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List The total number and dollar value of transactions that happened within a date range"
        )
@api_view(['GET'])
@req_keys_check(keys=["low_date", "high_date"])
def find_purchase_count_amount(request):
    """
    {
        low_date:"2021-03-10"
        high_date:"2021-04-10"
    }
    """
    req_low_date = request.query_params.get('low_date')
    req_high_date = request.query_params.get('high_date')

    result = PurchaseHistory.objects \
             .list_purchase_count_amount(
             req_low_date, req_high_date)

    return Response({
        "result": result,
        "request_data": request.query_params
    })

@swagger_auto_schema(method ='get', operation_summary="List The total number and dollar value of transactions that happened within a date range")
@swagger_auto_schema(method='post',operation_summary="Edit book store name, book name, book price and user name")
# GET, POST bookstorename, bookname, bookprice, username
@api_view(['GET', 'POST'])
def list_bsname_bookname_bookprice_username(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'GET':
        serializer = UpdateSerializer(user)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UpdateSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List The most popular book stores by transaction volume, either by number of transactions or transaction dollar value"
        )
@api_view(['GET'])
def find_popular_bookstore(request):
    from django.db.models import Count, Sum

    result = BookStore.objects.values('name').annotate(
               amount_count=Count('book__price'),total_price=Sum('book__price')
               ).latest('amount_count', 'total_price')
    
    return Response(result)


@swagger_auto_schema(
        methods=['get'], 
        operation_summary="List Total number of users who made transactions above or below $v within a date range"
        )
@api_view(['GET'])
@req_keys_check(keys=["amount", "compare", "low_date", "high_date"])
@req_params_in_key_check(params={"compare": ["larger", "smaller"]})
def find_date_range_user_total(request):
    """
    {
        amount: 10,
        compare: larger,
        low_date: "2020-02-10",
        high_date: "2020-04-27",
    }
    """
    req_amount = request.query_params.get('amount')
    req_compare = request.query_params.get('compare')
    req_low_date = request.query_params.get('low_date')
    req_high_date = request.query_params.get('high_date')

    result = User.objects.list_date_range_user_total(
             req_amount, req_compare, req_low_date, req_high_date
             )

    return Response({
        "result": result,
        "request_data": request.query_params
    })


# transaction
@swagger_auto_schema(
        methods=['post'], 
        operation_summary="Process a user purchasing a book from a book store, handling all relevant data changes in an atomic transaction"
        )
@api_view(["POST"])
@req_keys_check(keys=["user", "book"])
def find_user_purchase_process(request):

    data = json.loads(request.body)
    user = data['user']
    book = data['book']

    result = User_Purchase(user, book)

    return Response({
        "result": result,
        "request_data": request.query_params
    })
