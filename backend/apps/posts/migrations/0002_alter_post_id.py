# Generated by Django 4.1.6 on 2023-04-02 01:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.CharField(
                default="b81a8ef3-fe4f-4f7a-919e-10b8e3f209f0",
                editable=False,
                max_length=256,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]