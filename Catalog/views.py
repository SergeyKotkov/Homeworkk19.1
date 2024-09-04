from django.shortcuts import render
from Catalog.models import Category, Product

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def category(request):
    return render(request, 'Category.html')

def catalog(request):
    categories = Product.objects.all()
    return render(request, 'Category_list.html', {'categories': categories})

def Category_detail(request, pk):
        context = {
            'Products': Product.objects.get(pk=pk)
        }
        return render(request, 'Category_detail.html', context)
