from django.shortcuts import render
from main.models import InventoryItem

def show_inventory(request):
    initial_inventory_data = InventoryItem.objects.all()
    context = {
        'list_items': initial_inventory_data,
        'name': 'Muhammad Hilal Darul Fauzan',
        'id': '2206830542'
    }
    return render(request, 'main.html', context)