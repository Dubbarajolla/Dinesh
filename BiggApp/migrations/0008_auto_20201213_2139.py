# Generated by Django 3.1.2 on 2020-12-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiggApp', '0007_my_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerce',
            name='image',
            field=models.FileField(upload_to='pictures'),
        ),
    ]