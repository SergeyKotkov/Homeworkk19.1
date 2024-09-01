from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/', views.category, name='category'),
    path('catalog/', views.catalog, name='catalog'),
]

