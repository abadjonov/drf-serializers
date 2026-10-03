from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Yangi rasm qo'shish uchun bo'sh joylar soni
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return ""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image_preview']
    inlines = [ProductImageInline]

    def image_preview(self, obj):
        if obj.images.first():
            return mark_safe(f'<img src="{obj.images.first().image.url}" width="100" height="100"/>')
        return ""
