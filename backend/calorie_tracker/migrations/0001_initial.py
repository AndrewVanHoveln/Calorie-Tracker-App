# Generated by Django 5.0.6 on 2024-05-18 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('session_cookie', models.CharField(max_length=64, null=True)),
                ('session_expiration', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('food', models.CharField(max_length=100)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fats', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorie_tracker.user')),
            ],
        ),
    ]