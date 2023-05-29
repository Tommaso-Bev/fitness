from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class workout(models.Model):
   workout_name=models.CharField(max_length=25, unique=True)
   muscle_plan=models.CharField(max_length=25)
   description=models.CharField(max_length=300)
   image=models.ImageField(upload_to='img')
   
class workout_plan(models.Model):
   username=models.CharField(max_length=128)
   workout_name=models.CharField(max_length=25)
   progress=models.IntegerField(default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
   ])
