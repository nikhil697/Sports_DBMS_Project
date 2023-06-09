# Generated by Django 4.1.6 on 2023-03-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "Enrollment_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=30)),
                ("Phone_number", models.IntegerField(max_length=9, unique=True)),
                (
                    "Fine",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                ("Item1", models.IntegerField(null=True)),
                ("Item2", models.IntegerField(null=True)),
                ("Item3", models.IntegerField(null=True)),
            ],
        ),
    ]
