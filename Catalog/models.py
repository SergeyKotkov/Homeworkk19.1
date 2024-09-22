from django.db import models
NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='контент')
    preview = models.ImageField(upload_to='blog/image/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')


    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version')
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
        ordering = ['version_name']

    def __str__(self):
        return f'{self.version_number} {self.version_name}'
