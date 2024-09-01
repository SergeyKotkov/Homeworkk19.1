from django.shortcuts import render
from Catalog.models import Category, Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def category(request):
    return render(request, 'Category.html')

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'Category.html', {'categories': categories})

