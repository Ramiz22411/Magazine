from django.contrib import admin
from .models import Category, Product


# Register your models here.
#
# admin.site.register(Category)
# admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name']


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount', ]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category', 'quantity']
    fields = ['name', 'category', 'slug', 'description', 'image', ('price', 'discount'), 'quantity']
