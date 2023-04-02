# Generated by Django 4.1.5 on 2023-04-02 04:12

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default='fd026ff2-68b5-43ac-8753-c869167bba49', editable=False, max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('source', models.CharField(blank=True, max_length=256, null=True)),
                ('origin', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('contentType', models.CharField(choices=[('text/plain', 'text/plain'), ('text/markdown', 'text/markdown'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/plain', max_length=20)),
                ('content', models.TextField()),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, size=None)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE')], default='PUBLIC', max_length=10)),
                ('unlisted', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['published'],
            },
        ),
    ]
