# Generated by Django 5.0.7 on 2024-09-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("model_prediction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="cd_account",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="customer",
            name="credit_card",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="customer",
            name="online",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="customer",
            name="securities_account",
            field=models.IntegerField(),
        ),
    ]
