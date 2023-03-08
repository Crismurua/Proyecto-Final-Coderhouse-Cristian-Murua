from django.test import TestCase, Client
from .models import Product
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
                username = 'User',
                password = 'password',
                email = 'user@email.com',
            )
        self.product1 = Product.objects.create(
            name = 'Product1',
            description = 'Description1',
            price = 130,
            location = 'Buenos Aires',
            available = True,
            user = self.user
        )
        
    def test_module(self):
        self.assertEquals(self.product1.name, 'Product1')
        self.assertEquals(self.product1.description, 'Description1')
        self.assertEquals(self.user.email, 'user@email.com')
        self.assertEquals(self.user.username, 'User')
        
    def test_home_route(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)
        
    def test_login_template(self):
        response = self.client.get("http://127.0.0.1:8000/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
    def test_register_and_login(self):
        self.regiter_url = "http://127.0.0.1:8000/signup/"
        data = {
            'username': 'User',
            'password1': 'password123',
            'password2': 'password123',
            'email' : 'example@mail.com',
            'location' : 'Argentina',
            'phone' : 1123458876,
        }
        self.login_url = "http://127.0.0.1:8000/login/"
        response_register = self.client.post(self.regiter_url, data, format='json')
        response = self.client.post(self.login_url, username=self.user.username, password=self.user.password)
        self.assertEqual(response_register.status_code, 200)
        self.assertEqual(response.status_code, 200)
        