# Generated by Django 5.1.5 on 2025-02-04 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Signup',
        ),
    ]
