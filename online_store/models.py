from django.db import models
import uuid
from rest_framework_api_key.models import AbstractAPIKey

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    requisites = models.CharField(max_length=20)
    card_type = models.CharField(max_length=50)
    is_authenticated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClientAPIKey(AbstractAPIKey):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="api_keys",
        verbose_name="Клиент"
    )


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="users")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="stores")
    product = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Order #{self.id} - {self.product}"


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="users_comment")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="stores_comment")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders_comment")
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Review #{self.review_id} - Rating: {self.rating}"