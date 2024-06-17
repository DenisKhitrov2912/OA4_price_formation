from rest_framework.test import APITestCase, APIClient

from users.models import User
from price.models import Price
from django.urls import reverse
from rest_framework import status


class PriceTestCase(APITestCase):
    """Тестирование цен"""

    def setUp(self) -> None:
        """Создание условий для теста"""
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com',
                                        password='12345', )
        self.client.force_authenticate(user=self.user)
        self.price = Price.objects.create(user=self.user, start_price='100')

    def test_create_price(self):
        """Тест создания"""
        data = {
            'user': self.user.id,
            'start_price': '200'}
        response = self.client.post(reverse('price:price_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {'user': self.price.user.id,
                          'shipper': None,
                          'start_price': '200.00',
                          'final_price': '272.00'})

    def test_retrieve_price(self):
        """Тест одной цены"""
        response = self.client.get(
            reverse('price:price', kwargs={'pk': self.price.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'user': self.price.user.id,
                          'shipper': None,
                          'start_price': '100.00',
                          'final_price': '136.00'})

    def test_update_price(self):
        """Тест обновления"""
        data = {
            'shipper': '123'
        }
        response = self.client.patch(
            reverse('price:price_update', kwargs={'pk': self.price.pk}),

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'user': self.price.user.id,
             'shipper': '123',
             'start_price': '100.00',
             'final_price': '136.00'}
        )

    def test_delete_price(self):
        """Тест удаления"""
        response = self.client.delete(
            reverse('price:price_delete', kwargs={'pk': self.price.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_validators(self):
        """Тест валидатора цены"""
        data = {
            'start_price': '-100'
        }
        response = self.client.patch(
            reverse('price:price_update', kwargs={'pk': self.price.pk}),

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            ["Укажите положительную цену."]
        )
