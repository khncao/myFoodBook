# Generated by Django 3.1.3 on 2020-11-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBookApp', '0012_auto_20201115_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
