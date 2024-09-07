from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from Catalog.models import Category, Product, Blog


#def home(request):
 #   return render(request, 'home.html')

#def contacts(request):
#    return render(request, 'contacts.html')

#def category(request):
#    return render(request, 'Category.html')

#def Catalog(request):
#    categories = Product.objects.all()
#    return render(request, 'product_list.html', {'categories': categories})

#def Category_detail(request, pk):
#        context = {
#            'Products': Product.objects.get(pk=pk)
#        }
#        return render(request, 'product_detail.html', context)

class CategoryDetailViews(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class contactsTemplateView(TemplateView):
    template_name = 'contacts.html'

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.счетчик_просмотров += 1
        self.object.save()
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "description", "image", "category", "price")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog

    def get_success_url(self):

        return reverse('your_success_url_name', args=[self.object.pk])
