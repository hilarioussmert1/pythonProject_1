# Generated by Django 4.2.7 on 2023-12-19 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0009_remove_product_material_product_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simpleapp.material'),
        ),
    ]