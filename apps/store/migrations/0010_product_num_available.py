# Generated by Django 3.1 on 2020-09-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_available',
            field=models.IntegerField(default=1),
        ),
    ]
