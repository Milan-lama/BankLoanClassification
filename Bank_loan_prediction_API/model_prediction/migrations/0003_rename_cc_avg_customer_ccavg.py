# Generated by Django 5.0.7 on 2024-09-09 14:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "model_prediction",
            "0002_alter_customer_cd_account_alter_customer_credit_card_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="cc_avg",
            new_name="ccavg",
        ),
    ]
