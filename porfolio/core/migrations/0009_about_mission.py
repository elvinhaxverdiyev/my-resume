# Generated by Django 5.1.5 on 2025-01-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_home_rol1_home_rol2_home_rol3'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='mission',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
