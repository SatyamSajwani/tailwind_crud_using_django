# Generated by Django 5.1.4 on 2024-12-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_phone_color_alter_phone_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]