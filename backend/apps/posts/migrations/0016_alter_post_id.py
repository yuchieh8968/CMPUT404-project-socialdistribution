# Generated by Django 4.1.5 on 2023-04-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='21b8c3a5-2b47-4e6d-89b8-ad57c8e1f7a0', editable=False, max_length=256, primary_key=True, serialize=False),
        ),
    ]
