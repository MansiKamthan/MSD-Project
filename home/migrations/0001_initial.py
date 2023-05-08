# Generated by Django 3.2.10 on 2023-05-06 04:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('available', 'AVAILABLE'), ('pending', 'PENDING'), ('sold', 'SOLD')], default='none', max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=3)),
                ('square_feet', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('featured_property', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='False')),
                ('property_image_main', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
                ('property_image_1', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
                ('property_image_2', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
                ('property_image_3', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyNeighborhood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_neighborhood_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPricerange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_price_range_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('property_neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertyneighborhood')),
                ('property_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertytype')),
                ('property_type_price_range', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertypricerange')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_listing_image_main', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
                ('property_listing_image_All', models.ImageField(blank=True, upload_to='media/property_images/%Y/%m/%d/')),
                ('property_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='property_neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertyneighborhood'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertytype'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type_price_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.propertypricerange'),
        ),
    ]