# Generated by Django 3.2.3 on 2021-09-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='customer',
            field=models.ManyToManyField(blank=True, to='postapp.Customer'),
        ),
    ]
