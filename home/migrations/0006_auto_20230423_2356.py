# Generated by Django 3.2.10 on 2023-04-24 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_propertyimage_property_image_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='property_listing_image_all',
            new_name='property_listing_image_All',
        ),
        migrations.RemoveField(
            model_name='propertyimage',
            name='property_image_type',
        ),
    ]
