# Generated by Django 5.1.5 on 2025-01-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_home_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='role',
        ),
        migrations.AddField(
            model_name='home',
            name='role',
            field=models.ManyToManyField(blank=True, to='core.role'),
        ),
    ]
