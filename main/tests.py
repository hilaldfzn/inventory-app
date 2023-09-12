from django.test import TestCase, Client
from main.models import InventoryItem

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_response_has_utf8_charset(self):
        response = Client().get('/main/')
        content_type = response.get('Content-Type', '')
        self.assertIn('utf-8', content_type.lower())
    
    def test_inventory_items_displayed(self):
        response = self.client.get('/main/')
        for item in InventoryItem.objects.all():
            self.assertContains(response, item.name)
            self.assertContains(response, f'{item.price} BP')
            self.assertContains(response, item.category)

    def test_inventory_items_not_displayed(self):
        InventoryItem.objects.all().delete()
        response = self.client.get('/main/')
        for item in InventoryItem.objects.all():
            self.assertNotContains(response, item.name)
    
    def test_inventory_items_creation(self):
        item = InventoryItem.objects.create(
            name='War Cry',
            amount=3,
            description='The new charging heavy attack is different between swords and polearms. The charge before the weapon attack will also stagger enemies, but does not deal any damage.',
            price=7500,
            power=100,
            category='Ashes of War',
        )

        self.assertEqual(item.name, 'War Cry')
        self.assertEqual(item.amount, 3)
        self.assertEqual(item.description, 'The new charging heavy attack is different between swords and polearms. The charge before the weapon attack will also stagger enemies, but does not deal any damage.')
        self.assertEqual(item.price, 7500)
        self.assertEqual(item.power, 100)
        self.assertEqual(item.category, 'Ashes of War')