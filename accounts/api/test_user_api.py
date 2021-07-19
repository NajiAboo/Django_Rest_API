from rest_framework.test import APITestCase

from rest_framework import status
from rest_framework.reverse import reverse as api_reverse



# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='cfe', email="n@test.com")
        user.set_password("mytest")
        user.save()
        
    def test_created_user(self):
        qs = User.objects.filter(username='cfe')
        self.assertEqual(qs.count(), 1)
    
    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'cfe.doe',
            'email':'cfe.doe@gmail.com',
            'password': 'learncode'                
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.Http_400_BAD_REQUEST)