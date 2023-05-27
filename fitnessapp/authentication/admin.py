
# Register your models here.
from django.contrib import admin

from .models import workout,workout_plan


admin.site.register(workout)
admin.site.register(workout_plan)