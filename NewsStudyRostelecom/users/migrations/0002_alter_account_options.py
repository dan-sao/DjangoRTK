# Generated by Django 4.2.6 on 2023-12-01 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['user'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
