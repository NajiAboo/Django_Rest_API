from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='cfe', email="n@test.com")
        user.set_password("mytest")
        user.save()
        
    def test_created_user(self):
        qs = User.objects.filter(username='cfe')
        self.assertEqual(qs.count(), 1)