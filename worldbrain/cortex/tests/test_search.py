from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SearchTests(APITestCase):
    def test_search(self):
        url = reverse('api:search-list')
        data = {'q': 'very_unique_title',
                'domain_name': 'domain_name',
                'size': '10',
                'from': '0'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
