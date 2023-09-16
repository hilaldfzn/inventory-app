from django.contrib import admin
from main.models import InventoryItem

# Register your models here.
@admin.register(InventoryItem)

class InventoryItem(admin.ModelAdmin):
    list_display = ('name', 'amount', 'description', 'price', 'power', 'category')
    list_filter = ('description'),