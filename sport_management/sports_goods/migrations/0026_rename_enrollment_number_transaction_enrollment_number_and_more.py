# Generated by Django 4.1.6 on 2023-04-30 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0025_remove_transaction_fine"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="enrollment_number",
            new_name="Enrollment_number",
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="item_code",
            new_name="id",
        ),
    ]
