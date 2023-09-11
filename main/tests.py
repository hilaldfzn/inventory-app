from django.test import TestCase, Client

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
    
    def test_item_detail(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Katana')
        self.assertContains(response, 10)
        self.assertContains(response, 'Katana is a sword with a curved blade longer than 60 cm fitted with an uchigatana-style mounting and worn in a waist sash with the cutting edge facing up.')
        self.assertContains(response, 'Rp. 5000000,-')
        self.assertContains(response, '75')
        self.assertContains(response, 'Melee')