# Generated by Django 5.0.4 on 2024-04-30 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applies',
            new_name='Apply',
        ),
        migrations.RenameModel(
            old_name='Positions',
            new_name='Position',
        ),
    ]
