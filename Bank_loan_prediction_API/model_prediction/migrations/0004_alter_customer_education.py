# Generated by Django 5.0.7 on 2024-09-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("model_prediction", "0003_rename_cc_avg_customer_ccavg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="education",
            field=models.IntegerField(max_length=20),
        ),
    ]
