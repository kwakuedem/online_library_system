# Generated by Django 5.0.2 on 2024-02-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_student_approved_student_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
