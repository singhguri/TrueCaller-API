# Generated by Django 3.0.7 on 2020-06-20 21:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('phnNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('isSpam', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('phnNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('isSpam', models.BooleanField(default=False)),
                ('isRegistered', models.BooleanField(default=False)),
            ],
        ),
    ]