from django.contrib import admin

from .models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'representative', 'contract_date', 'bought_product')

    list_filter = ('bought_product', 'contract_date', 'representative')

    search_fields = ('name', 'description')

    prepopulated_fields = {'slug': ('name',)}

    date_hierarchy = 'contract_date'

    ordering = ('representative', 'contract_date', 'bought_product')
