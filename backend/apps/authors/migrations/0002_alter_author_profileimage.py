# Generated by Django 4.1.6 on 2023-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]