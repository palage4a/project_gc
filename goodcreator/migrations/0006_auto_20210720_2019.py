# Generated by Django 3.2.5 on 2021-07-20 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodcreator', '0005_auto_20210720_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='updated_ad',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='updated_ad',
        ),
    ]