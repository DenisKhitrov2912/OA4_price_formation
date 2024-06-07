# Generated by Django 5.0.6 on 2024-06-07 10:03

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_alter_price_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='bank_comission',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.02'), max_digits=5, verbose_name='комиссия банку'),
        ),
        migrations.AlterField(
            model_name='price',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='конечная цена'),
        ),
        migrations.AlterField(
            model_name='price',
            name='market_comission',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.20'), max_digits=5, verbose_name='комиссия маркетплейса'),
        ),
        migrations.AlterField(
            model_name='price',
            name='shipper_comission',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.08'), max_digits=5, verbose_name='комиссия за перевод поставщику'),
        ),
        migrations.AlterField(
            model_name='price',
            name='start_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='начальная цена'),
        ),
        migrations.AlterField(
            model_name='price',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.06'), max_digits=5, verbose_name='общий налог'),
        ),
    ]