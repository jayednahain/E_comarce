# Generated by Django 3.2.9 on 2021-12-05 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_porduct_sulg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='porduct',
            old_name='sulg',
            new_name='slug',
        ),
    ]
