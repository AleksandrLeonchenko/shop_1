# Generated by Django 4.2.3 on 2023-09-24 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCost', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PaymentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=8, unique=True, verbose_name='Номер карты')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('month', models.CharField(max_length=2, verbose_name='Месяц')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('code', models.CharField(max_length=3, verbose_name='Код')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards2', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Параметры карты оплаты',
                'verbose_name_plural': 'Параметры карт оплаты',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время формирования заказа')),
                ('deliveryType', models.IntegerField(choices=[(1, 'Доставка'), (2, 'Экспресс-доставка')], default=1, null=True, verbose_name='Способ доставки')),
                ('paymentType', models.IntegerField(choices=[(1, 'Онлайн картой'), (2, 'Онлайн со случайного чужого счёта')], default=1, null=True, verbose_name='Способ оплаты')),
                ('totalCost', models.FloatField(default=1)),
                ('status', models.IntegerField(choices=[(1, 'ожидание платежа'), (2, 'оплачено')], default=1, null=True, verbose_name='Статус заказа')),
                ('city', models.CharField(default='yyy', max_length=100)),
                ('address', models.CharField(default='xxx', max_length=100)),
                ('basket', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_orders.basket', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items2', to='app_orders.basket', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_basketitem2', to='app_products.productinstance', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Продукт в корзине',
                'verbose_name_plural': 'Продукты в корзине',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(through='app_orders.BasketItem', to='app_products.productinstance', verbose_name='Выбранные товары'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket2', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]