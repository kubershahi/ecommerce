# Generated by Django 2.2.5 on 2019-10-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20191012_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]