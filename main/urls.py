from django.urls import path
from main.views import show_inventory, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_items, dec_items, remove_items

app_name = 'main'

urlpatterns = [
    path('', show_inventory, name='show_inventory'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_items/<int:item_id>/', add_items, name='add_items'),
    path('dec_items/<int:item_id>/', dec_items, name='dec_items'),
    path('remove_items/<int:item_id>/', remove_items, name='remove_items'),
]