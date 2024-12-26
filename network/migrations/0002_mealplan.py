# Generated by Django 5.1.1 on 2024-12-04 10:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('activity_level', models.CharField(choices=[('sedentary', 'Sedentary'), ('lightly_active', 'Lightly Active'), ('moderately_active', 'Moderately Active'), ('very_active', 'Very Active')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]