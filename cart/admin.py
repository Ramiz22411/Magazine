from django.contrib import admin
from .models import Cart, CartQuerySet


# Register your models here.
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ['product', 'quantity', 'created_at']
    search_fields = ['product', 'quantity', 'created_at']
    readonly_fields = ('created_at',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_at']
    list_filter = ['created_at', 'user', 'product__name']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Anonymous user!'

    def product_display(self, obj):
        return str(obj.product.name)
