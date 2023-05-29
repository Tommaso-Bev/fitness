from django import forms
from .models import workout_plan

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = workout_plan
        fields = ['username', 'workout_name']