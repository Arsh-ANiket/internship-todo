# Generated by Django 5.0.3 on 2024-04-18 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210322_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
    ]
