from django.contrib import admin
from product.models import Category, Product, Gallery


class GalleryAdmin(admin.TabularInline):
    list_display = ["product", "image"]
    model = Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product", "category"]

    inlines = [GalleryAdmin]


admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
