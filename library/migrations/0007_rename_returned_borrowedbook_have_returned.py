# Generated by Django 5.0.2 on 2024-02-25 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_borrowedbook_returned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='returned',
            new_name='have_returned',
        ),
    ]
