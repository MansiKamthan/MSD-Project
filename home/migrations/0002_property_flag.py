# Generated by Django 3.2.10 on 2023-05-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]