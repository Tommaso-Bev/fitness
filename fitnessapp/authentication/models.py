from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
   image1 = models.ImageField(upload_to='workout_images', default='workout_images\not_found_prova_2bv4so2.png')
   image2 = models.ImageField(upload_to='workout_images', default='workout_images\not_found_prova_2bv4so2.png')
   image3 = models.ImageField(upload_to='workout_images', default='workout_images\not_found_prova_2bv4so2.png')
   image4 = models.ImageField(upload_to='workout_images', default='workout_images\not_found_prova_2bv4so2.png')

class history_per_workout(models.Model):
   username=models.ForeignKey(User, on_delete=models.CASCADE)  
   workout_name=models.ForeignKey(workout, on_delete=models.CASCADE)
   level=models.IntegerField(default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
   ])
   date=models.DateField()