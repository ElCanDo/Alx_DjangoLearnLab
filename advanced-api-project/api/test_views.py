from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class BookViewTests(APITestCase):
    def setUp(self):
        #createna a testbuser in the test database
        self.user = User.objects.create_user(
            username ="booktester",
            password="booktestpass321"
        )
    def test_list_book(self):
        self.client.login(username ="booktester",
            password="booktestpass321")
        
        url = reverse("books")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_book(self):
        self.client.login(username ="booktester",
            password="booktestpass321")
        data = {"title":"ElCando's Journey", "publication_year": 2025, "author":"ElCanDo"}
        url = reverse("books")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
