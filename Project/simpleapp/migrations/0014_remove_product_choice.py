# Generated by Django 4.2.7 on 2023-12-19 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0013_alter_product_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='choice',
        ),
    ]
