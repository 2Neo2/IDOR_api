# -*- coding: utf-8 -*-


from online_store.models import Store, Client, Order, Review
from django.core.management.base import BaseCommand
import json
from django.utils.dateparse import parse_datetime
import uuid

class Command(BaseCommand):
    help = 'Заполнение БД'

    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def handle(self, *args, **options):
        stores = self.load_json('json/stores.json')
        users = self.load_json('json/users.json')
        orders = self.load_json('json/orders.json')
        reviews = self.load_json('json/reviews.json')
        
        for store in stores:
            if not Store.objects.filter(name=store['name']).exists():
                Store.objects.create(
                    store_id=store['store_id'],
                    name=store['name'],
                    location=store['location'],
                    category=store['category']
                )

        for user in users:
            if not Client.objects.filter(id=user['id']).exists():
                Client.objects.create(
                    id=user['id'],
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    email=user['email'],
                    address=user['address'],
                    requisites=user['requisites'],
                    card_type=user['card_type']
                )
    
        for order in orders:
            if not Order.objects.filter(id=order['id']).exists():
                try:
                    client = Client.objects.get(id=order['user'])
                    store = Store.objects.get(store_id=order['store'])
                    Order.objects.create(
                        id=order['id'],
                        user=client,
                        store=store,
                        product=order['product'],
                        amount=order['amount'],
                        status=order['status'],
                        created_at=parse_datetime(order['created_at'])
                    )
                except (Client.DoesNotExist, Store.DoesNotExist) as e:
                    print(f"Пропущен заказ {order['id']}: {e}")

        for review in reviews:
            if not Review.objects.filter(review_id=review['id']).exists():
                try:
                    client = Client.objects.get(id=review['user'])
                    store = Store.objects.get(store_id=review['store'])
                    order = Order.objects.get(id=review['order'])
                    Review.objects.create(
                        review_id=review['id'],
                        user=client,
                        store=store,
                        order=order,
                        rating=review['rating'],
                        comment=review['comment'],
                        created_at=parse_datetime(review['created_at'])
                    )
                except (Client.DoesNotExist, Store.DoesNotExist, Order.DoesNotExist) as e:
                    print(f"Пропущен отзыв {review['id']}: {e}")



















