from rest_framework import serializers

from price.models import Price


class PriceSerializer(serializers.ModelSerializer):
    """Сериализатор цен"""

    class Meta:
        model = Price
        fields = '__all__'
