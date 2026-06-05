from django.urls import path
from . import views
from bitbox import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_product, name='search'),
    path('support/', views.user_support, name='support'),
]