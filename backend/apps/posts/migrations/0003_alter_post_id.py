# Generated by Django 4.1.6 on 2023-03-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_alter_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.CharField(
                default="2ed503a7-c3a5-4aa8-a924-0c476902bd10",
                editable=False,
                max_length=256,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]