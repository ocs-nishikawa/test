# Generated by Django 3.2.2 on 2021-06-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.TextField(blank=True),
        ),
    ]
