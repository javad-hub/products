# Generated by Django 3.2.3 on 2021-05-17 15:09

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
                ('name', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=400)),
                ('Image', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
