# Generated by Django 3.2.3 on 2021-05-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
    ]
