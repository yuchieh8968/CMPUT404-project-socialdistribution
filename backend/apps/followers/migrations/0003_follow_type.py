# Generated by Django 4.1.6 on 2023-04-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("followers", "0002_alter_follow_actor_alter_follow_object"),
    ]

    operations = [
        migrations.AddField(
            model_name="follow",
            name="type",
            field=models.CharField(default="Follow", max_length=20),
        ),
    ]