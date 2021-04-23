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
]
