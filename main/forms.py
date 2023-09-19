from django.forms import ModelForm
from main.models import InventoryItem

class ProductForm(ModelForm):
    class Meta:
        model = InventoryItem
        fields = ["name", "category", "amount", "power", "price", "description"]