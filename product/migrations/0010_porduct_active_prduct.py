# Generated by Django 3.2.9 on 2021-12-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rename_active_porduct_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='porduct',
            name='active_prduct',
            field=models.BooleanField(default=True),
        ),
    ]
