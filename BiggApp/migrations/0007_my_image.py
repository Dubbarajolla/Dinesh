# Generated by Django 3.1.2 on 2020-12-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
       ('BiggApp', '0006_auto_20201123_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Photos')),
                ('Name', models.CharField(max_length=150)),
            ],
        ),
    ]