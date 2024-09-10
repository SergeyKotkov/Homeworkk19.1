from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ProductListView, CategoryDetailViews, HomeTemplateView, contactsTemplateView, BlogListView, \
    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, tuggle_Blog

app_name = 'Catalog'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', contactsTemplateView.as_view(), name='contacts'),
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('Category_detail/<int:pk>', CategoryDetailViews.as_view(), name='Category_detail'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_form/', BlogCreateView.as_view(), name='blog_form'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('activity/<int:pk>', tuggle_Blog, name='toggle_activity'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

