from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class workout(models.Model):
   workout_name=models.CharField(max_length=25, unique=True, verbose_name="workout")
   muscle_plan=models.CharField(max_length=25)
   description=models.CharField(max_length=300)
   image=models.ImageField(upload_to='img')

   def __str__(self):
      return self.workout_name
   
   
class workout_plan(models.Model):
   username=models.CharField(max_length=128)
   workout_name=models.CharField(max_length=25)

   progress=models.IntegerField(default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
   ])

class workout_level(models.Model):
   workout_name=models.ForeignKey(workout, on_delete=models.CASCADE)
   level=models.IntegerField(default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
   ])
   image1 = models.ImageField(upload_to='workout_images')
   image2 = models.ImageField(upload_to='workout_images')
   image3 = models.ImageField(upload_to='workout_images')
   image4 = models.ImageField(upload_to='workout_images')