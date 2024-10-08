from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from Catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from Catalog.models import Product, Blog, Version
from Catalog.services import get_product_from_cache


class CategoryDetailViews(DetailView):
    model = Product


class ProductListView(ListView, LoginRequiredMixin):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_product_from_cache()
        return context_data


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'Catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('Catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('Catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("Catalog.can_edit_is_published") and user.has_perm(
                "Catalog.can_edit_description") and user.has_perm("Catalog.can_edit_category") and user:
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('Catalog:product_list')


def tuggle_Product(reqest, pk):
    product_name = get_object_or_404(Product, pk=pk)
    if product_name.is_published:
        product_name.is_published = False
    else:
        product_name.is_published = True

    product_name.save()

    return redirect(reverse('Catalog:product_list'))


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class contactsTemplateView(TemplateView):
    template_name = 'contacts.html'


class BlogListView(ListView, LoginRequiredMixin):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView, LoginRequiredMixin):
    model = Blog
    template_name = 'Catalog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Blog
    fields = ("title", "slug", "body", "preview", "created_at", "is_published")
    success_url = reverse_lazy('Catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView, LoginRequiredMixin):
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


class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('Catalog:blog_list')


def tuggle_Blog(request, pk):
    blog_title = get_object_or_404(Blog, pk=pk)
    if blog_title.is_published:
        blog_title.is_published = False
    else:
        blog_title.is_published = True

    blog_title.save()

    return redirect(reverse('Catalog:blog_list'))
