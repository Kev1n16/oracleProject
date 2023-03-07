from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import main, login, create, flavor

class TestUrls(SimpleTestCase):

    def test_main_url_is_resolved(self):
        url = reverse('main page')
        print(resolve(url))
        self.assertEquals(resolve(url).func, main)

    def test_login_url_is_resolved(self):
        url = reverse('login page')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_create_url_is_resolved(self):
        url = reverse('Create account page')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create)

    def test_flavor_url_is_resolved(self):
        url = reverse('flavor')
        print(resolve(url))
        self.assertEquals(resolve(url).func, flavor)