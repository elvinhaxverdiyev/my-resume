# Generated by Django 5.1.5 on 2025-02-02 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
    ]
