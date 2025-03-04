# Generated by Django 4.1.6 on 2023-04-03 06:38



from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(max_length=20, unique=True)),
                ("displayName", models.CharField(max_length=20)),
                ("github", models.URLField(blank=True, max_length=255, null=True)),
                ("profileImage", models.URLField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["displayName"],
            },
        ),
    ]
