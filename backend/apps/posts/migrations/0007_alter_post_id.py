# Generated by Django 4.1.5 on 2023-03-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='33f85dcd-e03f-4acd-9159-2065ba36d97d', editable=False, max_length=256, primary_key=True, serialize=False),
        ),
    ]
