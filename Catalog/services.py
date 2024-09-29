from django.core.cache import cache

from Catalog.models import Product
from config.settings import CACHE_ENABLED

def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all
    key = "Product_list"
    product = cache.get(key)
    if product is not None:
        return product
    products = Product.objects.all
    cache.set(key, products)
    return products