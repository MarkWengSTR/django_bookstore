from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('find_store_open_at/', views.find_store_open_at,
         name='find_store_open_at'),
    path('find_store_open_weekday_at/', views.find_store_open_weekday_at,
         name='find_store_open_weekday_at'),
    path('find_store_with_open_hour/', views.find_store_with_open_hour,
         name='find_store_with_open_hour'),
    path('find_books_in_price_range/', views.find_books_in_price_range,
         name='find_books_in_price_range'),
    path('find_bookstore_by_book_num/', views.find_bookstore_have_num_of_books,
         name='find_bookstore_by_book_num'),
    path('find_bookstore_by_book_num_price_range/', views.find_bs_have_num_of_books_price_range,
         name='find_bookstore_by_book_num_price_range'),
    path('find_book_or_store_by_name/', views.search_b_bs_by_name,
         name='find_book_or_store_by_name'),
    path('find_user_date_range_amount/', views.find_user_date_range_amount,
         name='find_user_date_range_amount'),
    path('find_purchase_count_amount/', views.find_purchase_count_amount,
         name='find_purchase_count_amount'),
    path('find_bsname_bookname_bookprice_username/list/<str:pk>/', views.list_bsname_bookname_bookprice_username,
            name="list_bsname_bookname_bookprice_username"),
    path('find_popular_bookstore/', views.find_popular_bookstore, name="find_popular_bookstore"),
    path('find_date_range_user_total/', views.find_date_range_user_total, name="find_date_range_user_total"),
    path('find_user_purchase_process/', views.find_user_purchase_process, name="find_user_purchase_process"),
]
