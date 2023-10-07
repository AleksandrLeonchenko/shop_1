# Generated by Django 4.2.3 on 2023-09-24 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название категории продукта')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории продукта')),
            ],
            options={
                'verbose_name': 'Категория продукта',
                'verbose_name_plural': 'Категории продукта',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CategoryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(blank=True, default='images/no_image.jpg', null=True, upload_to='images/images_product/', verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Альтернативная строка изображения продукта')),
            ],
            options={
                'verbose_name': 'Изображение категории',
                'verbose_name_plural': 'Изображения категорий',
            },
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название продукта')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL продукта')),
                ('item_number', models.IntegerField(default=True, verbose_name='Артикул продукта')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Краткое описание продукта')),
                ('fullDescription', models.TextField(blank=True, verbose_name='Полное описание продукта')),
                ('freeDelivery', models.BooleanField(default=False, verbose_name='free delivery')),
                ('sort_index', models.PositiveIntegerField(default=True, verbose_name='Индекс сортировки')),
                ('number_of_purchases', models.PositiveIntegerField(default=True, verbose_name='Количество покупок')),
                ('limited_edition', models.BooleanField(default=False, null=True, verbose_name='Ограниченный тираж')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена продукта')),
                ('salePrice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Цена продукта при распродаже')),
                ('count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество продукта на складе')),
                ('available', models.BooleanField(default=True, null=True, verbose_name='Доступность продукта в каталоге')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения продукта')),
                ('dateFrom', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала распродажи продукта')),
                ('dateTo', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания распродажи продукта')),
                ('archived', models.BooleanField(default=True, verbose_name='Продукт архивирован')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True, verbose_name='Рейтинг продукта')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category2', to='app_products.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Значение рейтинга',
                'verbose_name_plural': 'Значения рейтинга',
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=5000, verbose_name='Текст отзыва')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения отзыва')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author_review2', to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_review2', to='app_products.review', verbose_name='Родительский отзыв')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews2', to='app_products.productinstance', verbose_name='Продукт')),
                ('rate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review2', to='app_products.rate', verbose_name='Значение рейтинга')),
            ],
            options={
                'verbose_name': 'Отзыв к продукту',
                'verbose_name_plural': 'Отзывы к продукту',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='PropertyTypeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название характеристики продукта')),
                ('slug', models.SlugField(max_length=200, verbose_name='URL характеристики продукта')),
                ('category', models.ManyToManyField(related_name='propertyType_category2', to='app_products.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Название характеристики продукта',
                'verbose_name_plural': 'Названия характеристик продукта',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PropertyInstanceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=200, verbose_name='Значение характеристики')),
                ('slug', models.SlugField(max_length=200, verbose_name='URL значения характеристики')),
                ('name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='propertyInstance_propertyType2', to='app_products.propertytypeproduct', verbose_name='Название характеристики продукта')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specifications2', to='app_products.productinstance', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Значение характеристики продукта',
                'verbose_name_plural': 'Значения характеристик продуктов',
                'ordering': ('value',),
            },
        ),
        migrations.AddField(
            model_name='productinstance',
            name='tags',
            field=models.ManyToManyField(related_name='tag2', to='app_products.tag', verbose_name='Теги продукта'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(blank=True, default='images/no_image.jpg', null=True, upload_to='images/images_product/', verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Альтернативная строка изображения продукта')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images2', to='app_products.productinstance', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Изображение продукта',
                'verbose_name_plural': 'Изображения продуктов',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image2', to='app_products.categoryimages', verbose_name='Изображение категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories2', to='app_products.category', verbose_name='Родительская категория'),
        ),
        migrations.AddIndex(
            model_name='productinstance',
            index=models.Index(fields=['id', 'slug'], name='app_product_id_45c445_idx'),
        ),
    ]