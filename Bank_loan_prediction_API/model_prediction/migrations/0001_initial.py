# Generated by Django 5.0.7 on 2024-09-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField()),
                ("experience", models.IntegerField()),
                ("income", models.FloatField()),
                ("family", models.IntegerField()),
                ("cc_avg", models.FloatField()),
                ("mortgage", models.FloatField()),
                ("zip_code", models.CharField(max_length=10)),
                ("home_ownership", models.CharField(max_length=20)),
                ("education", models.CharField(max_length=20)),
                ("securities_account", models.BooleanField(default=False)),
                ("cd_account", models.BooleanField(default=False)),
                ("online", models.BooleanField(default=False)),
                ("credit_card", models.BooleanField(default=False)),
                ("gender", models.CharField(max_length=10)),
            ],
        ),
    ]
