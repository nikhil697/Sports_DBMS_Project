# Generated by Django 4.1.6 on 2023-04-01 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0014_alter_ptudents_table"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ptudents",
            new_name="Students",
        ),
    ]
