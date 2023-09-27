from urllib import response
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_valid_form(self):
        data = {
                'author_class': 'PBP D',
                }
        response = self.client.post('/main/', data)
        
        # Mengecek bahwa data dari context sesuai dengan ekspektasi
        self.assertEqual(response.context['author_name'], 'Khansa Mahira')
        self.assertEqual(response.context['author_class'], 'PBP D')