# Generated by Django 5.0.7 on 2024-08-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_amenity_created_at_amenity_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=180),
        ),
    ]
