# from django.shortcuts import render
# def customer_lists(request):
#     customers = [
#         {'name' : 'Toma Shelby'},
#         {'name' : 'Will Smith'},
#     ]
#     return render(request, 'customer_list.html', {'customers': customers})

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
import africastalking
from decouple import config

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]


AT_username = config('AT_username')
AT_apiKey =   config('AT_apiKey')

# print(f"Username: {AT_username}")
# print(f"API Key: {AT_apiKey}")

africastalking.initialize(AT_username, AT_apiKey)

# africastalking.initialize(os.environ.get('AT_username'),os.environ.get('AT_apiKey'))
sms = africastalking.SMS

def send_sms(phone_number, message):
    try:
         
        response = sms.send(message,[phone_number])
        print(f"SMS Response: {response}")  # Print the response to check
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        print(f"Sending SMS to: {customer.phone_number}")  # Print the phone number for debugging
        response = send_sms(customer.phone_number, f"Order {order.item} created with amount {order.amount}")
        print(f"SMS API Response: {response}")
        
        send_sms(customer.phone_number, f"Your Order for {order.item} has been created with amount {order.amount} at {order.time}")

        return super().perform_create(serializer)