# Generated by Django 4.2.7 on 2023-11-29 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(default=1000)),
                ('user_telegram_chat_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tennis_user_profiles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'db_table': 'tennis_users',
            },
        ),
    ]
