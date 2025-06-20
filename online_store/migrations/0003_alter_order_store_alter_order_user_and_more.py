# Generated by Django 5.0.8 on 2025-06-11 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_store", "0002_clientapikey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stores",
                to="online_store.store",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="online_store.client",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders_comment",
                to="online_store.order",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stores_comment",
                to="online_store.store",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_comment",
                to="online_store.client",
            ),
        ),
    ]
