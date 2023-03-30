# Generated by Django 4.1.6 on 2023-03-30 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("likes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
