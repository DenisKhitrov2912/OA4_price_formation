# Generated by Django 5.0.6 on 2024-06-07 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField(verbose_name='начальная цена')),
                ('product', models.CharField(blank=True, max_length=200, null=True, verbose_name='товар')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='дата создания/изменения')),
                ('shipper', models.CharField(blank=True, max_length=200, null=True, verbose_name='поставщик')),
                ('tax', models.SmallIntegerField(default=0.06, verbose_name='общий налог')),
                ('bank_comission', models.SmallIntegerField(default=0.02, verbose_name='комиссия банку')),
                ('shipper_comission', models.SmallIntegerField(default=0.08, verbose_name='комиссия за перевод поставщику')),
                ('market_comission', models.SmallIntegerField(default=0.2, verbose_name='миссия маркетплейса')),
                ('final_price', models.IntegerField(verbose_name='конечная цена')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'цена',
                'verbose_name_plural': 'цены',
            },
        ),
    ]
