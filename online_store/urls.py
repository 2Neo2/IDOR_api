from django.urls import path
from .views import (
    StoreListView,
    StoreDetailView,

    ClientListView,
    ClientDetailView,

    OrderListView,
    OrderDetailView,

    ReviewListView,
    ReviewDetailView
)

urlpatterns = [
    path('clients', ClientListView.as_view(), name='user-list'),
    path('clients/<str:pk>', ClientDetailView.as_view(), name='user-detail'),

    path('stores', StoreListView.as_view(), name='store-list'),
    path('stores/<int:pk>', StoreDetailView.as_view(), name='store-detail'),

    path('orders', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),

    path('reviews', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]