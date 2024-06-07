from django.urls import path

from price.apps import PriceConfig
from price.views import (PriceCreateAPIView, PriceListAPIView,
                         PriceDetailAPIView, PriceUpdateAPIView,
                         PriceDestroyAPIView)

app_name = PriceConfig.name

urlpatterns = [
    path('price/create/', PriceCreateAPIView.as_view(), name='price_create'),
    path('', PriceListAPIView.as_view(), name='prices'),
    path('price/<int:pk>/', PriceDetailAPIView.as_view(), name='price'),
    path('price/update/<int:pk>/', PriceUpdateAPIView.as_view(),
         name='price_update'),
    path('price/delete/<int:pk>/', PriceDestroyAPIView.as_view(),
         name='price_delete'),
]
