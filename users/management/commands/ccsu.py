from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда на создание суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.ru',
            is_superuser=True,
            is_active=True,
            is_staff=True,
            is_trader=True,
        )
        user.set_password('1234567')
        user.save()
