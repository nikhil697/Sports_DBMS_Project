# Generated by Django 4.1.6 on 2023-04-30 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0023_alter_students_fine"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("transaction_id", models.AutoField(primary_key=True, serialize=False)),
                ("time_of_booking", models.DateTimeField(auto_now_add=True)),
                ("time_of_release", models.DateTimeField(blank=True, null=True)),
                (
                    "fine",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
                ),
                (
                    "enrollment_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sports_goods.students",
                    ),
                ),
                (
                    "item_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sports_goods.goods",
                    ),
                ),
            ],
            options={
                "db_table": "Transaction",
            },
        ),
    ]
