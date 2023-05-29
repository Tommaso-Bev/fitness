from django.db import models

class workout(models.Model):
   workout_name=models.CharField(max_length=25, unique=True)
   muscle_plan=models.CharField(max_length=25)
   description=models.CharField(max_length=300)
   image=models.ImageField(upload_to='img')
   
class workout_plan(models.Model):
   username=models.CharField(max_length=128, unique=True)
   wourkout_name=models.CharField(max_length=25)
