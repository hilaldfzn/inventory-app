import datetime
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.forms import ProductForm
from main.models import InventoryItem

@login_required(login_url='/login')
def show_inventory(request):
    items = InventoryItem.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'creator': 'Muhammad Hilal Darul Fauzan',
        'id' : '2206830542',
        'class' : 'PBP C',
        'list_items' : items,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_inventory'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    # Get product berdasarkan ID
    product = InventoryItem.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_inventory'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

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

def get_product_json(request):
    product_item = InventoryItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_inventory")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')

    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def add_amount(request, item_id):
    if request.method == 'POST':
        item = InventoryItem.objects.get(pk=item_id)
        item.user = request.user
        if item.amount > 0:
            item.amount += 1
            item.save()
        return HttpResponse(b"ADDED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def decrease_amount(request, item_id):
    if request.method == 'POST':
        item = InventoryItem.objects.get(pk=item_id)
        item.user = request.user
        if item.amount > 1:
            item.amount -= 1
            item.save()
        else:
            item.delete()
        return HttpResponse(b"REDUCED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def remove_items(request, item_id):
    if request.method == "DELETE":
        item = InventoryItem.objects.get(pk=item_id, user=request.user)
        item.delete()
        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        power = request.POST.get("power")
        category = request.POST.get("category")
        user = request.user

        new_product = InventoryItem(name=name, amount=amount, description=description, 
                                    price=price, power=power, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = InventoryItem.objects.create(
            user = request.user,
            name = data["name"],
            category = data["category"],
            amount = int(data["amount"]),
            power = int(data["power"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)