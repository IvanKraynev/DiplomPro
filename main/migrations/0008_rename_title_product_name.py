# Generated by Django 5.0.6 on 2024-06-25 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order_cartitem_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
