from django.urls import path, include
from authentication import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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
    path('workhistory', views.workhistory, name='workhistory'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)