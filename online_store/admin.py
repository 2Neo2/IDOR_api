from django.contrib import admin
from .models import *
from rest_framework_api_key.models import APIKey


try:
    admin.site.unregister(APIKey)
except admin.sites.NotRegistered:
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_authenticated']
    readonly_fields = ['id', 'first_name', 'last_name', 'email', 'address', 'requisites', 'card_type', 'is_authenticated']

    fieldsets = (
        (
            'Информация', {'fields': ('id', 'first_name', 'last_name', 'is_authenticated')}
        ),
        (
            'Адреса', {'fields': ('email', 'address')}
        ),
        (
            'Финансы', {'fields': ('requisites', 'card_type')}
        ),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_id', 'name']
    readonly_fields = ['store_id', 'name', 'location', 'category']

    fieldsets = (
        (
            'Информация', {'fields': ('store_id', 'name', 'category')}
        ),
        (
            'Адреса', {'fields': ('location',)}
        ),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'store', 'status', 'created_at']
    readonly_fields = ['id', 'user', 'store', 'product', 'amount', 'status', 'created_at']

    fieldsets = (
        (
            'Информация', {'fields': ('id', 'user')}
        ),
        (
            'Магазин', {'fields': ('store', 'product', 'amount')}
        ),
        (
            'Данные по покупке', {'fields': ('status', 'created_at')}
        ),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'user', 'rating']
    readonly_fields = ['review_id', 'user', 'store', 'order', 'rating', 'comment', 'created_at']

    fieldsets = (
        (
            'Информация', {'fields': ('review_id', 'user', 'store', 'order')}
        ),
        (
            'Отзыв', {'fields': ('rating', 'comment')}
        ),
        (
            'Настройки', {'fields': ('created_at',)}
        ),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
