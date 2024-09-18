from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ProductListView, CategoryDetailViews, HomeTemplateView, contactsTemplateView, BlogListView, \
    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, tuggle_Blog, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductDetailView, tuggle_Product

app_name = 'Catalog'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', contactsTemplateView.as_view(), name='contacts'),
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='Product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('activity/<int:pk>', tuggle_Product, name='toggle_activity'),
    path('Category_detail/<int:pk>', CategoryDetailViews.as_view(), name='Category_detail'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_form/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('activity/<int:pk>', tuggle_Blog, name='toggle_activity'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

