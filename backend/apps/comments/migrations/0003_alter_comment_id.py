# Generated by Django 4.1.6 on 2023-03-28 22:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0002_alter_comment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]