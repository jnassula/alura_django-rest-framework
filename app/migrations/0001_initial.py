# Generated by Django 4.1.2 on 2022-10-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("code", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=255)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("B", "Basic"),
                            ("I", "Intermediate"),
                            ("A", "Advanced"),
                        ],
                        default="B",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=30)),
                ("rg", models.CharField(max_length=9)),
                ("cpf", models.CharField(max_length=11)),
                ("birth_date", models.DateField()),
            ],
        ),
    ]