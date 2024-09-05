from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('Category_list/', views.catalog, name='Category_list'),
    path('Category_detail/<int:pk>', views.Category_detail, name='Category_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

