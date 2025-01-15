# Generated by Django 2.2.5 on 2019-10-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191011_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='Age',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.TextField(max_length=20, null=True),
        ),
    ]