# Generated by Django 4.2.7 on 2023-12-20 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0016_remove_product_material_product_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='choice',
        ),
    ]