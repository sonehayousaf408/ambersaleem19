# Generated by Django 5.2.3 on 2025-07-02 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_rename_total_sale_amount_sale_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='library.customer'),
        ),
    ]
