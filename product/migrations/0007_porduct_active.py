# Generated by Django 3.2.9 on 2021-12-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_sulg_porduct_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='porduct',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
