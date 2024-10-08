# Generated by Django 4.2.2 on 2024-09-28 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Catalog', '0010_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите продавца', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец'),
        ),
    ]
