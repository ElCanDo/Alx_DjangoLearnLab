from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class BookViewTests(APITestCase):
    def test_list_book(self):
        url = reverse("books")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_book(self):
        data = {"title":"ElCando's Journey", "publication_year": 2025, "author":"ElCanDo"}
        url = reverse("books")
        response = self.client.post(url, data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Optionally, assert on response.data if needed, e.g.:
        self.assertEqual(response.data["title"], data["title"])
