from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import InventoryItem
from django.urls import reverse
from django.shortcuts import render

def show_inventory(request):
    items = InventoryItem.objects.all()

    context = {
        'creator' : 'Muhammad Hilal Darul Fauzan',
        'id' : '2206830542',
        'class' : 'PBP C',
        'list_items' : items,
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_inventory'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = InventoryItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = InventoryItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = InventoryItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = InventoryItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")