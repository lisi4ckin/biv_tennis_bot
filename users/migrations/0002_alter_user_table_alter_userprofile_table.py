# Generated by Django 4.2.7 on 2023-11-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='tennis_users',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='tennis_user_profiles',
        ),
    ]
