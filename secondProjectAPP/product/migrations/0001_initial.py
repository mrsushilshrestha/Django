# Generated by Django 5.1.5 on 2025-01-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(max_length=100)),
                ('product_name', models.TextField(max_length=255)),
                ('product_price', models.IntegerField(max_length=100)),
                ('product_type', models.TextField(max_length=255)),
                ('product_date', models.DateTimeField(auto_now=True)),
                ('product_weight', models.IntegerField(max_length=100)),
            ],
        ),
    ]
