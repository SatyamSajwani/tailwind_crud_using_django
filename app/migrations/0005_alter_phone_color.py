# Generated by Django 5.1.4 on 2024-12-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_phone_cetegory_alter_phone_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='color',
            field=models.CharField(choices=[('select', 'Select'), ('silver', 'Silver'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('orange', 'Orange')], default='select', max_length=20),
        ),
    ]
