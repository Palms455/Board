# Generated by Django 3.0.2 on 2020-01-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_item_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='photo',
            field=models.ImageField(upload_to='item_photo/'),
        ),
    ]
