# Generated by Django 4.1.6 on 2023-04-03 06:38



from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Inbox",
            fields=[
                ("sender", models.URLField(max_length=512)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("url", models.URLField(max_length=512)),
                ("contentType", models.CharField(blank=True, max_length=20)),
                ("summary", models.CharField(blank=True, max_length=512)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
