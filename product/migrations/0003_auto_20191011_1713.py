# Generated by Django 2.2.5 on 2019-10-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191011_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
