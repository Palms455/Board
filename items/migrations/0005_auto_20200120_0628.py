# Generated by Django 3.0.2 on 2020-01-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20200118_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Название'),
        ),
    ]
