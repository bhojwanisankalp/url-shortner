from django.http import response
from .models import Url
from django.test import TestCase, Client

# Create your tests here.


class TestShortner(TestCase):
    def setUp(self):
        self.client = Client()
        
        url_one = Url.objects.create(
            original_url="https://wikipedia.com", 
            slug="trgsheoruhtnqe", 
            name="external")
        
        url_two = Url.objects.create(
            original_url="http://localhost:8000/url-to-test", 
            slug="trgsheoruhtnql", 
            name="local")
    
    def test_shortner(self):
        response = self.client.post('/short-url')
        self.assertEquals(response.status_code, 200)

    def test_url_creation(self):
        one = Url.objects.get(slug ='trgsheoruhtnqe')
        two = Url.objects.get(slug ='trgsheoruhtnql')
        print(one.original_url)
        print(two.original_url)
    
    def test_local_url_redirect(self):
        two = Url.objects.get(slug ='trgsheoruhtnql')
        response = self.client.get(f'u/{two.slug}')

        self.assertEquals(response.status_code, 200)
    
    def test_exteral_url_redirect(self):
        one = Url.objects.get(slug ='trgsheoruhtnqe')

        response = self.client.get(f'u/{one.slug}')

        self.assertEquals(response.status_code, 200)