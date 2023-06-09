# Generated by Django 4.2.1 on 2023-05-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="workout_plans",
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
                ("username", models.CharField(max_length=128, unique=True)),
                ("wourkout_name", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="workouts",
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
                ("wourkout_name", models.CharField(max_length=25, unique=True)),
                ("muscle_plan", models.CharField(max_length=25)),
                ("description", models.CharField(max_length=300)),
            ],
        ),
    ]
