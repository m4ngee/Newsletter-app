

from django.test import TestCase
from .models import Sub

class SubscriptionTest(TestCase):

    def test_valid_subscription(self):
        response = self.client.post('/subscribe/', {
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after success
        self.assertTrue(Sub.objects.filter(email='testuser@example.com').exists())

    def test_duplicate_email(self):
        Sub.objects.create(email='john@example.com')
        response = self.client.post('/subscribe/', {
            'email': 'john@example.com'
        })
        self.assertContains(response, 'This email is already subscribed.')
