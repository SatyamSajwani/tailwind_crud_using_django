# Generated by Django 5.1.4 on 2024-12-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_phone_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='cetegory',
            field=models.CharField(choices=[('select', 'Select'), ('leptop', 'Leptop'), ('ipad', 'Ipad'), ('phone', 'Phone'), ('watch', 'Watch')], default='select', max_length=25),
        ),
        migrations.AlterField(
            model_name='phone',
            name='color',
            field=models.CharField(choices=[('select', 'sSelect'), ('silver', 'Silver'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('orange', 'Orange')], default='select', max_length=20),
        ),
    ]
