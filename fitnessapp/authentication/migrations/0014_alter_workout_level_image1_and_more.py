# Generated by Django 4.2.1 on 2023-06-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0013_alter_workout_level_image1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workout_level",
            name="image1",
            field=models.ImageField(
                default="not_found_prova_2bv4so2.png", upload_to="workout_images"
            ),
        ),
        migrations.AlterField(
            model_name="workout_level",
            name="image2",
            field=models.ImageField(
                default="not_found_prova_2bv4so2.png", upload_to="workout_images"
            ),
        ),
        migrations.AlterField(
            model_name="workout_level",
            name="image3",
            field=models.ImageField(
                default="not_found_prova_2bv4so2.png", upload_to="workout_images"
            ),
        ),
        migrations.AlterField(
            model_name="workout_level",
            name="image4",
            field=models.ImageField(
                default="not_found_prova_2bv4so2.png", upload_to="workout_images"
            ),
        ),
    ]
