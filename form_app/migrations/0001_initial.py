# Generated by Django 3.0.3 on 2020-03-02 23:05

import ares_util.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jméno', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('ičo', models.PositiveIntegerField(validators=[ares_util.validators.czech_company_id_ares_api_validator])),
            ],
        ),
    ]
