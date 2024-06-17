from decimal import Decimal

from django.db import models

from price.validators import (validate_positive_price)

NULLABLE = {'blank': True, 'null': True}


class Price(models.Model):
    """Модель ценообразования"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             verbose_name='пользователь', **NULLABLE)
    start_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='начальная цена')
    product = models.CharField(max_length=200, verbose_name='товар',
                               **NULLABLE)
    date_time = models.DateTimeField(auto_now_add=True,
                                     verbose_name='дата создания/изменения')
    shipper = models.CharField(max_length=200, verbose_name='поставщик',
                               **NULLABLE)
    tax = models.DecimalField(max_digits=5, decimal_places=2,
                              default=Decimal('0.06'),
                              verbose_name='общий налог')
    bank_comission = models.DecimalField(max_digits=5, decimal_places=2,
                                         default=Decimal('0.02'),
                                         verbose_name='комиссия банку')
    shipper_comission = models.DecimalField(max_digits=5, decimal_places=2,
                                            default=Decimal('0.08'),
                                            # установлено свое
                                            # значение, в условии его нет
                                            verbose_name='комиссия за перевод '
                                                         'поставщику')
    market_comission = models.DecimalField(max_digits=5, decimal_places=2,
                                           default=Decimal('0.20'),
                                           verbose_name='комиссия '
                                                        'маркетплейса')
    final_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='конечная цена', **NULLABLE)

    def __str__(self):
        return f"""Поставщик: {self.user}
        Начальная цена: {self.start_price}
        Конечная цена: {self.final_price}"""

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'

    def clean(self):
        validate_positive_price(self)

    def save(self, *args, **kwargs):
        self.full_clean()
        self.final_price = self.start_price + (
                self.start_price * (self.tax + self.bank_comission +
                                    self.shipper_comission +
                                    self.market_comission))
        super(Price, self).save(*args, **kwargs)
