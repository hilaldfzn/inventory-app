from django.shortcuts import render

def show_inventory(request):
    context = {
        'name': 'Katana',
        'amount': 10,
        'description': 'Katana is a sword with a curved blade longer than 60 cm fitted with an uchigatana-style mounting and worn in a waist sash with the cutting edge facing up.',
        'price': 5000000,
        'power': 75,
        'category':'Melee'
    }

    return render(request, 'main.html', context)