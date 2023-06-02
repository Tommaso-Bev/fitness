# Generated by Django 4.2.1 on 2023-05-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0007_workout_plan_progress"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("image", models.ImageField(upload_to="img")),
            ],
        ),
        migrations.CreateModel(
            name="ImCar",
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
                ("workout_name", models.CharField(max_length=25)),
                ("images", models.ManyToManyField(to="authentication.imagemodel")),
            ],
        ),
    ]
