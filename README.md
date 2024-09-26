# CustomerOrderService
A Simple Customer and Orders Database 

# Overview
Customer Order Service is a Simple Python-based application that provides an API to manage customers and orders. It supports adding, retrieving, and processing customer orders, and sends SMS notifications when an order is placed using Africa’s Talking SMS gateway.

The project includes authentication via OpenID Connect, unit tests with coverage checks, and a CI/CD pipeline for automated deployment to AWS Elastic Beanstalk.

# Features
* REST API to manage customers and orders
* Authentication and authorization via OpenID Connect
* SMS notifications using Africa’s Talking API
* Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions
* Hosted on AWS Elastic Beanstalk
# Project Architecture
* Service: Python backend for customers and orders management.
* Database: Stores customers and orders using SQLite Database.
* API: REST endpoints to interact with the system.
* Authentication: Secured via OpenID Connect.
* SMS Alerts: Africa’s Talking integration to send notifications when an order is placed.
* Deployment: Deployed on AWS Elastic Beanstalk, integrated with CI/CD pipeline.
# Installation
# Prerequisites
* Python 3.1xx
* Django Rest Framework
* AWS CLI
* Africa’s Talking account for SMS services
* OpenID Connect provider for authentication
# Clone the repository
```
git clone https://github.com/OllieToo16/CustomerOrderService.git
cd CustomerOrderService
```

# Create and Activate Virtual Environment
```
python -m venv env
.\env\Scripts\activate
```
# Install dependencies
```
pip install django djangorestframework
pip install africastalking
pip install python-decouple

```
# Setup environment variables
* Create a .env file in the root directory and add the following:
```
AT_username=<your_africastallking_username>
AT_apiKey=<your_africastalking_api_key>
```
# Implementing Authentication with OAuth2 and OpenID Connect
* To protect the API using OpenID Connect for authentication:
* Install django-oidc-provider or use a library like django-allauth that supports OpenID Connect.
```
pip install django-oauth-toolkit
```
* Create a super user and provide credentials to authenticate and authorize
  ```
  python manage.py createsuperuser
  ```
* Login to the Django Admin using the credentials created
  ![image](https://github.com/user-attachments/assets/224472d3-b230-4043-adbf-2b3fca776c8f)

* Add an application and copy the client ID and client secret which you will use to get the access token
  ![image](https://github.com/user-attachments/assets/cdce279e-ba69-4e0b-a9e6-15b51c71e959)

* Go to your root directory of the project and get the access token using the following command:
```
  curl -X POST -d "grant_type=password&username=<your_username>&password=<password_created>&client_id=<Your_client_ID>&client_secret=<your_client_secret_id" http://localhost:8000/o/token/
 ```
* Add you access token key to the .env file:
  ```
  # Access token for authentication
  Acess_token=<your_access_token>
  ```
# Run the application
```
python manage.py migrate
python manage.py runserver
```
# API Endpoints
# Customer API
* POST /CustomerApp/customers/: Create a new customer
* GET /CustomerApp/customers/: Get a list of customers
  ![image](https://github.com/user-attachments/assets/a46b14c0-db87-4bc7-a5d9-671dedb8e44c)

* GET /CustomerApp/customers/{id}/: Get details of a specific customer
# Order API
* POST /CustomerApp/orders/: Create a new order
* GET /CustomerApp/orders/: Get a list of orders
  ![image](https://github.com/user-attachments/assets/70462f66-2f41-4752-a9ec-fd9451ab5ae9)

* GET /CustomerApp/orders/{id}/: Get details of a specific order

# Testing
* Run Unit Tests with Coverage
  ```
  python -m coverage run manage.py test
  python -m coverage report
  ```
# Deployment
  * Deploy to AWS Elastic Beanstalk
The project includes a GitHub Actions workflow to automatically deploy changes to AWS Elastic Beanstalk. Ensure you have set the following secrets in your GitHub repository:
  * AWS_ACCESS_KEY_ID
  * AWS_SECRET_ACCESS_KEY
  * EB_APP_NAME
  * EB_ENV_NAME

To deploy:

* Push your changes to the main branch.
* The GitHub Actions workflow will trigger and deploy your application to AWS.
You can also manually deploy by running:
```
eb init -p python-3.11 customerservice-app --region <your-region>
eb create customerservice-env
eb deploy
```
# SMS Alerts
* When an order is placed, an SMS notification is sent to the customer using the Africa's Talking API.As illustrated below:
  ![image](https://github.com/user-attachments/assets/d434ffb0-dd11-48fc-889d-696f08809b8f)

# Contribution
Contributions are welcome! Please follow these steps:
* Fork the repository.
* Create a new branch.
* Make your changes.
* Create a pull request.


  





