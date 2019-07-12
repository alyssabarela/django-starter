from rest_framework import status
from web.models import Placeholder
from django.urls import reverse
from rest_framework.test import APITestCase


class PlaceholderTests(APITestCase):
    def test_get(self):
        url = reverse('placeholder-list')
        data = {
          "data": {
            "type": "Placeholder",
            "attributes": {
              "placeholder": "Ember Hamster",
            },
            "relationships": {
              }
            }
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Placeholder.objects.count(), 1)
        self.assertEqual(Placeholder.objects.get().placeholder, 'thing')
