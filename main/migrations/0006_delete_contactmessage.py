# Generated by Django 5.0.6 on 2024-06-25 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
