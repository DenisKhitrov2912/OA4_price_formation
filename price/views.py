from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from price.models import Price
from price.serializers import PriceSerializer
from users.permissions import IsUserOwner, IsUserTrader


class PriceCreateAPIView(generics.CreateAPIView):
    """Создание цены"""
    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticated, IsUserTrader]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PriceListAPIView(generics.ListAPIView):
    """Список цен"""
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsUserTrader]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Price.objects.all()
        else:
            return Price.objects.filter(user=user)


class PriceDetailAPIView(generics.RetrieveAPIView):
    """Одна цена"""
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsUserTrader, IsUserOwner]


class PriceUpdateAPIView(generics.UpdateAPIView):
    """Обновление цены"""
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsUserTrader, IsUserOwner]


class PriceDestroyAPIView(generics.DestroyAPIView):
    """Удаление цены"""
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsUserTrader, IsUserOwner]
