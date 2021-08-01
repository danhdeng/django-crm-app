from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTestCase(TestCase):
    def test_landing_page(self):
        response=self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'leads/landing_page.html')
    
