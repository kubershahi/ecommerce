# Generated by Django 2.2.5 on 2019-10-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20191013_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]