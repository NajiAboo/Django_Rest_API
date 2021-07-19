from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Status

User = get_user_model()

# Create your tests here.
class StatusTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='cfe', email='test@gmail.com')
        user.set_password("naji")
        user.save()
    
    def test_creating_status(self):
        user = User.objects.get(username='cfe')
        obj = Status.objects.create(user=user, content='some cool')
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(),1)
        
        
        