# Generated by Django 4.2.7 on 2023-12-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpio', '0002_alter_button_gpio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpio',
            name='gpio',
            field=models.IntegerField(max_length=2, unique=True),
        ),
    ]
