# Generated by Django 5.0.1 on 2024-04-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_product_description_product_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Used'), (3, 'Scrapyard')], default=1),
        ),
    ]
