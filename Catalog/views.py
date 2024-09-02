from django.shortcuts import render, get_object_or_404
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

def Category_detail(request, pk):
    categories = get_object_or_404(Category, pk=pk)
    context = {'categories': categories}
    return render(request, 'Category_detail.html', context)

