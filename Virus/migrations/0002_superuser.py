# Generated by Django 3.1.2 on 2020-12-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Virus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='Super_users')),
            ],
        ),
    ]