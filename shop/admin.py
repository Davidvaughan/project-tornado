from django.contrib import admin

from .models import Category, Product, Images

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'display']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'price']

class ImagesAdmin(admin.ModelAdmin):

    list_display = ['name', 'product', 'image', 'display', 'main']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
