# Generated by Django 3.0.2 on 2020-01-18 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200118_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='number',
        ),
    ]
