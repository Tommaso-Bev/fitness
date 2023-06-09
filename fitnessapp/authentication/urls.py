from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('workouts', views.workouts, name="workouts"),
    path('register_workout/', views.register_workout, name='register_workout'),
    path('workoutprogression/<str:workout_name>/', views.workoutprogression, name='workoutprogression'),
    path('update-workout-plan/<str:workout_name>/', views.update_workout_plan, name='update_workout_plan'),
]