# # from django.test import TestCase

# # # Create your tests here.
# # # import sqlite3 
# # # import sqlite3
# # # # Connect to the SQLite database (ensure the file path is correct)
# # # conn = sqlite3.connect('db.sqlite')

# # # # Create a cursor object
# # # cursor = conn.cursor()

# # # # Query data from the 'customers' table
# # # cursor.execute("SELECT * FROM customers")
# # # customers = cursor.fetchall()

# # # # Query data from the 'orders' table
# # # cursor.execute("SELECT * FROM orders")
# # # orders = cursor.fetchall()

# # # # Print the data
# # # print("Customers:")
# # # for customer in customers:
# # #     print(customer)

# # # print("\nOrders:")
# # # for order in orders:
# # #     print(order)

# # # # Close the connection
# # # conn.close()


# from rest_framework.test import APITestCase
# from django.urls import reverse
# from .models import Customer

# class CustomerAPITestCase(APITestCase):

#     def setUp(self):
#     #     # Create a customer to be used in tests
#         self.customer = Customer.objects.create(name="Jane Doe", code="JD002")
        
#         # Get access token (assuming you have a valid user for testing)
#         self.token = 'DZbj08mUxFMLj9xAHmz4c3ydYXKKxm'

#     def get_access_token(self):
#         response = self.client.post('/o/token/', {
#             'grant_type': 'password',
#             'username': 'oliver.cheruiyot',  # replace with a valid username
#             'password': 'Pass123$',    # replace with the corresponding password
#             'client_id': 'kfmLjk2Fw8VN5jCgfnXi4o6rWM10ZCQi8mfPFl8s',  # replace with your client ID
#             'client_secret': 'X8Qoz5SHrrBO9rHdOUqtLuoFmhXsmuauYdY9qf6KpTi8Rl4EWtZpBf5eymuByG1H2ZYeMyWGXFIZkO7bS7bVQPtPTNtpf8VdeHIsORt1IM9X3cHHct0PYPTip0jTP5hW'
#         })
#         print("Response status code:", response.status_code)
#         print("Response data:", response.json)
#         if 'access_token' in response.json:

#             return response.json['access_token']  # Corrected to use json()
#         else:
#             raise ValueError("Access token not found in response")
            

#     def test_create_customer(self):
#         url = reverse('customer-list')  # Adjust this to your actual URL name
#         data = {"name": "John Doe", "code": "JD001", "phone_number": "+254762894033"}
        
#         # Set the authorization header
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 201)

#     def test_get_customers(self):
#         url = reverse('customer-list')  # Adjust this to your actual URL name
        
#         # Set the authorization header
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         if response.status_code != 200:
#             print(f"Failed to get access token. Status: {response.status_code}, Data: {response.json}")
#             raise ValueError("Failed to authenticate")

from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Customer

class CustomerAPITestCase(APITestCase):

    def setUp(self):
        # Create a customer to be used in tests
        self.customer = Customer.objects.create(name="Jane Doe", code="JD002", phone_number ="+254735675098")
        
        # Manually set a valid access token here
        self.token = 'DZbj08mUxFMLj9xAHmz4c3ydYXKKxm'  # Replace with a valid token

    def test_create_customer(self):
        url = reverse('customer-list')  # Adjust this to your actual URL name
        data = {
            "name": "John Doe",
            "code": "JD001",
            "phone_number": "+254762894033"
        }

        # Set the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token )
        
        response = self.client.post(url, data, format='json')
        
        # Check if the customer was created successfully
        self.assertEqual(response.status_code, 201)

    def test_get_customers(self):
        url = reverse('customer-list')  # Adjust this to your actual URL name
        
        # Set the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        response = self.client.get(url)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        # Optional: Print response data for debugging if necessary
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

