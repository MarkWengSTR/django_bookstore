from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore_api.utils.time import add_12_afternoon
from bookstore_api.models import BookStore, Book
# Create your views here.


@api_view(['GET'])
def show_index(request):
    return Response({
        "msg": "Hello!",
    })


@api_view(['GET'])
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


@api_view(['GET'])
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


@api_view(['GET'])
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


@api_view(['GET'])
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


@api_view(['GET'])
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
