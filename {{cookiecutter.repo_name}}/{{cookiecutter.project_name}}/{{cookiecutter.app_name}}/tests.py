import json

# from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import *
from .serializers import *

class TestExampleAppHStore(APITestCase):

    def setUp(self):
        # Create a user.
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(self.username,
            'testuser@example.com', self.password)
        token = Token.objects.create(user=self.user)
        self.token = token.key
        print self.token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    
    def test_hstore_field_api_create_string(self):
        response = self.client.post('/exampleapp/dummy/', {
            "msisdn": 1234,
            "product_code": "test_code",
            "data": '{ "a": "a", "b": "b" }'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        
        d = DummyModel.objects.last()
        self.assertEqual(d.msisdn, 1234)
        self.assertEqual(d.product_code, 'test_code')
        self.assertEqual(d.data, { 'a': 'a', 'b': 'b' })
    
    def test_hstore_field_api_create_json(self):
        post_data = {
            "msisdn": 1234,
            "product_code": "test_code",
            "data": { 'a': 'a', 'b': 2 }
        }
        response = self.client.post('/exampleapp/dummy/', json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        d = DataBag.objects.last()
        self.assertEqual(d.msisdn, 1234)
        self.assertEqual(d.product_code, 'test_code')
        self.assertEqual(d.data, { 'a': 'a', 'b': '2' })
    
    # def test_hstore_field_api_validation_error(self):
    #     response = self.client.post('/databag/', {
    #         "name": "test", 
    #         "data": "{ WRONG }"
    #     })
    #     self.assertEqual(response.status_code, 400)
        
    #     response = self.client.post('/databag/', {
    #         "name": "test", 
    #         "data": "true"
    #     })
    #     self.assertEqual(response.status_code, 400)
        
    #     response = self.client.post('/databag/', {
    #         "name": "test", 
    #         "data": "1"
    #     })
    #     self.assertEqual(response.status_code, 400)
    
    # def test_hstore_serializer(self):
    #     d = SchemaDataBag()
    #     d.name = 'test'
    #     d.number = 2
    #     d.float = 2.2
    #     d.boolean = True
    #     d.boolean_true = False
    #     d.char = 'char'
    #     d.text = 'text'
    #     d.date = datetime.date.today()
    #     d.datetime = datetime.datetime.now()
    #     d.decimal = 2.0
    #     d.email = 'test@test.com'
    #     d.ip = '10.10.10.10'
    #     d.url = 'http://test.com'
    #     d.full_clean()
    #     d.save()
        
    #     s = SchemaDataBagSerializer(instance=d).data
        
    #     self.assertEqual(s['name'], 'test')
    #     self.assertEqual(s['number'], 2)
    #     self.assertEqual(s['float'], 2.2)
    #     self.assertIs(s['boolean'], True)
    #     self.assertIs(s['boolean_true'], False)
    #     self.assertEqual(s['char'], 'char')
    #     self.assertEqual(s['text'], 'text')
    #     self.assertEqual(s['date'], d.date)
    #     self.assertEqual(s['datetime'], d.datetime)
    #     self.assertEqual(s['decimal'], 2.0)
    #     self.assertEqual(s['email'], 'test@test.com')
    #     self.assertEqual(s['ip'], '10.10.10.10')
    #     self.assertEqual(s['url'], 'http://test.com')
    #     # should be hidden
    #     self.assertTrue('data' not in s)
    
    # def test_hstore_serializer_validation(self):
    #     obj = SchemaDataBag()
    #     data = {
    #         "name": "test create", 
    #         "number": 'c',
    #         "float": 2.2,
    #         "boolean": True,
    #         "boolean_true": False,
    #         "char": "char",
    #         "text": "test create text",
    #         "choice": "choice2",
    #         "choice2": "choice1",
    #         "date": "2014-08-08",
    #         "datetime": "2014-08-08 14:10:53",
    #         "decimal": 1.0,
    #         "email": "WRONG",
    #         "ip": "10.10.10.10",
    #         "url": "WRONG"
    #     }
