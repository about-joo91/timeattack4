# Generated by Django 4.0.4 on 2022-06-03 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageModel',
        ),
    ]
