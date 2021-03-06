# Generated by Django 3.0.2 on 2020-01-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='currency',
            field=models.CharField(choices=[('CAD', 'Canadian Dollar'), ('USD', 'United States Dollar')], max_length=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PS', 'Processing'), ('BCO', 'Being Checked Out'), ('IP', 'Incomplete'), ('CP', 'Complete')], max_length=4),
        ),
    ]
