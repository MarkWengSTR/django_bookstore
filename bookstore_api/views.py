from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore_api.utils.time import add_12_afternoon
from bookstore_api.models import BookStore
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
