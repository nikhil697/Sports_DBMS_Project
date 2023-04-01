# Generated by Django 4.1.6 on 2023-03-31 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0006_ptudent_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "Enrollment_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=30)),
                ("Branch", models.CharField(default=None, max_length=30)),
                ("Phone_number", models.IntegerField(unique=True)),
                (
                    "Fine",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "Item1",
                    models.ForeignKey(
                        blank=True,
                        db_column="Item1",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item1_students",
                        to="sports_goods.goods",
                    ),
                ),
                (
                    "Item2",
                    models.ForeignKey(
                        blank=True,
                        db_column="Item2",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item2_students",
                        to="sports_goods.goods",
                    ),
                ),
                (
                    "Item3",
                    models.ForeignKey(
                        blank=True,
                        db_column="Item3",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item3_students",
                        to="sports_goods.goods",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Ptudent",
        ),
    ]
