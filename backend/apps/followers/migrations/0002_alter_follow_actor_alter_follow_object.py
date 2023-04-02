# Generated by Django 4.1.6 on 2023-04-02 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("followers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="actor",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="follow",
            name="object",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
