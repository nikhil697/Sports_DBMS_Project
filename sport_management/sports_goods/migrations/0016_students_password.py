# Generated by Django 4.1.6 on 2023-04-02 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0015_rename_ptudents_students"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="Password",
            field=models.CharField(
                default=12345,
                max_length=20,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
        ),
    ]
