# Generated by Django 4.1.5 on 2023-04-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='c7c7f3c1-3655-4b12-8719-92d99ce3376f', editable=False, max_length=256, primary_key=True, serialize=False),
        ),
    ]
