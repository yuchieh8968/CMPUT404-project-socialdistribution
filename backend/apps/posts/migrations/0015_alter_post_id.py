# Generated by Django 4.1.6 on 2023-04-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0014_alter_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.CharField(
                default="95c0dbb3-a77c-4810-a63b-d6fbeaa8f060",
                editable=False,
                max_length=256,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]