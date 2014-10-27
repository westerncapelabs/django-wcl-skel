import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


from .models import *
from .serializers import *



class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()


class AuthenticatedAPITestCase(APITestCase):

    def setUp(self):
        super(AuthenticatedAPITestCase, self).setUp()
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(self.username,
            'testuser@example.com', self.password)
        token = Token.objects.create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)



class TestExampleAppHStore(AuthenticatedAPITestCase):

    def test_login(self):
        request = self.client.post(
            '/{{cookiecutter.app_name}}/api-token-auth/', {"username": "testuser", "password": "testpass"})
        token = request.data.get('token', None)
        self.assertIsNotNone(
            token, "Could not receive authentication token on login post.")
        self.assertEqual(request.status_code, 200,
                         "Status code on /auth/login was %s (should be 200)." % request.status_code)

    def test_create_dummy_model_data(self):
        post_data = {
            "msisdn": 1234,
            "product_code": "test_code",
            "data": { 'a': 'a', 'b': 2 }
        }
        response = self.client.post('/{{cookiecutter.app_name}}/dummy/',
                                    json.dumps(post_data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = DummyModel.objects.last()
        self.assertEqual(d.msisdn, 1234)
        self.assertEqual(d.product_code, 'test_code')
        self.assertEqual(d.data, { 'a': 'a', 'b': '2' })

