import json
from django.core.management.base import BaseCommand
from Catalog.models import Category, Product

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('path/to/categories.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('path/to/products.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_for_create = []
        category_for_create = []
        for category_data in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name=category_data['fields']['name'],
                    description=category_data['fields']['description']
                )
            )

        Category.objects.bulk_create(category_for_create)
        for product_data in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product_data['fields']['name'],
                    description=product_data['fields']['description'],
                    category=Category.objects.get(pk=product_data['fields']['category'])
                )
            )

        Product.objects.bulk_create(product_for_create)
