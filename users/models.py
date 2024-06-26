from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default='True', verbose_name='активность')
    is_trader = models.BooleanField(
        default='False', verbose_name='продавец')  # назначить через админку
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
