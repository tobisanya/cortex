from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from worldbrain.cortex.models import Source

User = get_user_model()


class SourceTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='test',
            email='test@wordlbrain.io',
            password='testpassword'
        )
        super(SourceTests, self).setUp()

    def login(self, username, password):
        url = reverse('api-token')
        data = {
            "username": username,
            "password": password
        }
        response = self.client.post(url, data, format='json')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        return True

    def test_sources_without_auth(self):
        """
        Ensure that the source endpoint cannot be accessed without
        authorization.
        """
        url = reverse('api:source-list')
        data = {'domain_name': 'http://test.com'}
        get_response = self.client.get(url)
        post_response = self.client.post(url, data, format='json')
        self.assertEqual(get_response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(post_response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_create_sources(self):
        url = reverse('api:source-list')
        self.login('test', 'testpassword')

        empty = Source.objects.all()
        self.assertFalse(empty.exists(), "There should be no sources yet.")

        data = {'domain_name': 'http://test.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(Source.objects.count(), 1)
        self.assertEqual(Source.objects.get().domain_name, 'http://test.com')
