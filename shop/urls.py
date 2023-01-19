from django.urls import path

from . import views

urlpatterns = [
    path('category/<slug:slug>/', views.category_products),
    path('product/<slug:slug>/', views.product),
]
