# Generated by Django 5.0.1 on 2024-05-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_product_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]