# Generated by Django 4.2 on 2023-04-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usedproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
