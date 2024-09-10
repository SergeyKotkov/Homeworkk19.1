from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from Catalog.models import Category, Product, Blog


# def home(request):
#   return render(request, 'home.html')

# def contacts(request):
#    return render(request, 'contacts.html')

# def category(request):
#    return render(request, 'Category.html')

# def Catalog(request):
#    categories = Product.objects.all()
#    return render(request, 'product_list.html', {'categories': categories})

# def Category_detail(request, pk):
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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'Catalog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "slug", "body", "preview", "created_at", "is_published")
    success_url = reverse_lazy('Catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "slug", "body", "preview", "created_at", "is_published")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('Catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('Catalog:blog_list')


def tuggle_Blog(reqest, pk):
    blog_title = get_object_or_404(Blog, pk=pk)
    if blog_title.is_published:
        blog_title.is_published = False
    else:
        blog_title.is_published = True

    blog_title.save()

    return redirect(reverse('Catalog:blog_list'))
