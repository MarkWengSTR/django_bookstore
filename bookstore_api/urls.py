from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('find_store_open_at/', views.find_store_open_at,
         name='find_store_open_at'),
]
