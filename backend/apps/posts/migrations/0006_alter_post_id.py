# Generated by Django 4.1.6 on 2023-03-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_alter_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.CharField(
                default="86dd5f61-44f5-4165-b899-ae0223f6d755",
                editable=False,
                max_length=256,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]