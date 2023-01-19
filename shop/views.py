from django.shortcuts import render

from . models import Product, Category, Images

def category_products(request, slug):

    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category.id)

    return render(request, 'shop/category-products.html', {'products' : products})


def product(request, slug):

    product = Product.objects.get(slug=slug)
    mainImage = Images.objects.filter(product_id=product.id, main=True, display=True)

    return render(request, 'shop/product.html', {'product' : product, 'mainimage' : mainImage})
