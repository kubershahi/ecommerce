# Generated by Django 2.2.5 on 2019-10-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20191013_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
