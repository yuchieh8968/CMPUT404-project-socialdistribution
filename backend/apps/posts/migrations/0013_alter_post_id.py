

# Generated by Django 4.1.5 on 2023-04-01 00:59


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_id'),

    ]

    operations = [
        migrations.AlterField(

            model_name='post',
            name='id',
            field=models.CharField(default='c78d6a30-e1a1-465e-b1e9-2f4cd70d53af',
                                   editable=False, max_length=256, primary_key=True, serialize=False),

        ),
    ]
