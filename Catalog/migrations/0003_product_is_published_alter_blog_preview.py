# Generated by Django 5.1 on 2024-09-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog/image/', verbose_name='превью'),
        ),
    ]
