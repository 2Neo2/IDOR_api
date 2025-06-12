from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from .models import Client, ClientAPIKey, Order, Review, Store
import uuid

class IDORProtectionTests(APITestCase):
    def setUp(self):
        self.client1 = Client.objects.create(id=uuid.UUID("123e4567-e89b-12d3-a456-426614174000"), first_name="Brendan", last_name="Verrell", email="bverrell1@liveinternet.ru", address="PO Box 42021", requisites="4844131182932272", card_type="visa-electron")
        self.client2 = Client.objects.create(id=uuid.UUID("123e4567-e89b-12d3-a456-426614174001"), first_name="Imogen", last_name="Maddie", email="imaddie3@cbslocal.com", address="Suite 68", requisites="67626599591927797", card_type="maestro")
        
        self.store = Store.objects.create(store_id=1, name="Test Store", location="123 Main St", category="Electronics")

        self.order1 = Order.objects.create(id=10004, user=self.client1, store=self.store, product="Smartphone", amount=599.99, status="delivered", created_at=timezone.now())
        self.order2 = Order.objects.create(id=10010, user=self.client2, store=self.store, product="Laptop", amount=1099.99, status="processing", created_at=timezone.now())

        self.review1 = Review.objects.create(review_id=22, user=self.client1, store=self.store, order=self.order1, rating=5, comment="Excellent!", created_at=timezone.now())
        self.review2 = Review.objects.create(review_id=23, user=self.client2, store=self.store, order=self.order2, rating=3, comment="It was okay.", created_at=timezone.now())

        self.api_key1 = ClientAPIKey.objects.create_key(name="Key1", client=self.client1)[1]
        self.api_key2 = ClientAPIKey.objects.create_key(name="Key2", client=self.client2)[1]

    def test_user_cannot_access_foreign_order(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/orders/{self.order2.id}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_access_own_order(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/orders/{self.order1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_access_foreign_review(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/reviews/{self.review2.review_id}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_access_own_review(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/reviews/{self.review1.review_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_access_foreign_client(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/clients/{self.client2.id}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_access_own_client(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get(f'/api/clients/{self.client1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_clients_list_forbidden(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.api_key1}')
        response = self.client.get('/api/clients')
        self.assertIn(response.status_code, [status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_403_FORBIDDEN])
