# Generated by Django 5.0.8 on 2025-06-12 00:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_store", "0005_alter_client_is_authenticated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
