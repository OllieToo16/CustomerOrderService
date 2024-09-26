# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Customer
from decouple import config

# Create your tests here.

class CustomerAPITestCase(APITestCase):

    def setUp(self):
        # Create a customer to be used in tests
        self.customer = Customer.objects.create(name="Jane Doe", code="JD002", phone_number ="+254735675098")
        
        self.token = config('Access_token') 

    def test_create_customer(self):
        url = reverse('customer-list') 
        data = {
            "name": "John Doe",
            "code": "JD001",
            "phone_number": "+254762894033"
        }

        # Setting the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token )
        
        response = self.client.post(url, data, format='json')
        
        # Checking if the customer was created successfully
        self.assertEqual(response.status_code, 201)

    def test_get_customers(self):
        url = reverse('customer-list')  
        
        # Setting the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        response = self.client.get(url)
        
        # Checking if the request was successful
        self.assertEqual(response.status_code, 200)

        if response.status_code != 200:
            print(f"Failed to retrieve customers. Status: {response.status_code}, Data: {response.data}")
        
if __name__ == '__main__':
    import coverage
    cov = coverage.Coverage()
    cov.start()
    import unittest
    unittest.main()
    cov.stop()
    cov.save()
    cov.html_report(directory='coverage_html_report')

