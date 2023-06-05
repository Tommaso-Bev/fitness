
# Register your models here.
from django.contrib import admin

from .models import workout,workout_plan,workout_level


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout_name', 'muscle_plan', 'description')

class Workout_plan_Admin(admin.ModelAdmin):
    list_display = ('username', 'workout_name', 'progress')

class Workout_level_Admin(admin.ModelAdmin):
    list_display = ('workout_name', 'level')

admin.site.register(workout, WorkoutAdmin)
admin.site.register(workout_plan, Workout_plan_Admin)
admin.site.register(workout_level, Workout_level_Admin)
