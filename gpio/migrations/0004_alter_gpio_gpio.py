# Generated by Django 4.2.7 on 2023-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpio', '0003_alter_gpio_gpio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpio',
            name='gpio',
            field=models.IntegerField(max_length=2),
        ),
    ]