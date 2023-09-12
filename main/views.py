from django.shortcuts import render

def show_inventory(request):
    context = {
        'list_items': [
            {
                'name': 'Katana',
                'amount': 20,
                'description': 'Katana is a sword with a curved blade longer than 60 cm fitted with an uchigatana-style mounting and worn in a waist sash with the cutting edge facing up.',
                'price': 500,
                'power': 83,
                'category':'Melee Weapons'
            },
            {
                'name': 'Misbegotten Shortbow',
                'amount': 10,
                'description': 'Shortbow wielded by Winged Misbegotten. Fine fur clings to it. Designed to inflict additional damage by sacrificing range.',
                'price': 450,
                'power': 75,
                'category':'Ranged Weapons'
            },
            {
                'name': 'Cragblade',
                'amount': 43,
                'description': 'Dropped by a Teardrop Scarab in Caelid, west of the bridge leading towards Redmane Castle, behind the siege tower on a hill, right next to the monument.',
                'price': 300,
                'power': 63,
                'category':'Ashes of War'
            },
            {
                'name': 'Damascus Sword',
                'amount': 5,
                'description': 'Damascus steel swords were legendary for their great strength, durability and their “almost eternal” edge. They could cut silk as well as shatter a rock.',
                'price': 3000,
                'power': 100,
                'category':'Melee Weapons'
            },
            {
                'name': 'Shattershard Arrow',
                'amount': 107,
                'description': 'Arrow whittled from animal bones tipped with a shard of crystal. Creates a resonating noise at the point of impact.',
                'price': 150,
                'power': 40,
                'category':'Arrows'
            },
        ],
    }

    return render(request, 'main.html', context)