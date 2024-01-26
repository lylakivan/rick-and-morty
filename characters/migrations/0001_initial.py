# Generated by Django 5.0.1 on 2024-01-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Models",
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
                ("api_id", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Alive", "Alive"),
                            ("Dead", "Dead"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=50,
                    ),
                ),
                ("species", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Female", "Female"),
                            ("Male", "Male"),
                            ("Genderless", "Genderless"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=255,
                    ),
                ),
                ("images", models.URLField(max_length=255, unique=True)),
            ],
        ),
    ]
