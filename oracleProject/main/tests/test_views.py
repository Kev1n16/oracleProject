from django.test import TestCase, Client
from django.urls import reverse
from main.models import ToDoList, Item, Flavor
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.project1 = ToDoList.objects.create(
            name='testName'
        )

    def test_project_main_GET(self):
        response = self.client.get(reverse('main page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_project_login_GET(self):
        response = self.client.get(reverse('login page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_project_create_GET(self):
        response = self.client.get(reverse('Create account page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create/register.html')

    def test_project_flavor_GET(self):
        response = self.client.get(reverse('flavor'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'flavor/createflavor.html')

    def test_project_ToDoList_POST_adds_new_list(self):
        response = self.client.post(reverse('main page'),{
            'name': 'testName'
        })

        self.assertEquals(self.project1.name, 'testName')