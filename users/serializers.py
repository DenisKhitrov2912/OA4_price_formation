from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя для самого себя"""

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'city']


class UserSerializerForOthers(serializers.ModelSerializer):
    """Сериализатор пользователей общий"""

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city']
