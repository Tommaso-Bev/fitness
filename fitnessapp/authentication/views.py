from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from .models import workout, workout_plan, workout_level
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == 'POST':
       
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken, try with another')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists, try again')
            return redirect('signup')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')


        user = User.objects.create_user(username=username, email=email, password=password)
        
        return redirect('/login')

    return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User credentials are valid
            login(request, user)
            return redirect('/')
        else:
            # User credentials are invalid
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/')

def profile(request):
    user=request.user
    username=user.username
    email=user.email
    username = mark_safe(username)
    email = mark_safe(email)
    w_list=workout_plan.objects.filter(username=request.user.username)
    return render(request, "profile.html", {'username':username,'email':email, 'w_list': w_list})

def workouts(request):
    workout_list= workout.objects.all()
    return render(request, "workouts.html", {'workout_list': workout_list})

def register_workout(request):
    if request.method == 'POST':
        username=request.user.username
        workout_name=request.POST.get('workout_name')
        if workout_plan.objects.filter(username=username, workout_name=workout_name).exists():
            return redirect('workouts')
        workoutp=workout_plan(username=username, workout_name=workout_name)
        workoutp.save()
        return redirect('profile')
    return render(request, 'workouts.html')

def workoutprogression(request, workout_name):
    w = workout.objects.get(workout_name=workout_name)
    w_plan = workout_plan.objects.get(username=request.user.username, workout_name=workout_name)
    l = workout_level.objects.get(workout_name=w, level=w_plan.progress)
    show_button = w_plan.progress < 5

    return render(request, 'workoutprogression.html', {'w_plan': w_plan, 'w': w, 'w_level': l, 'show': show_button})


def update_workout_plan(request, workout_name):
    w = workout.objects.get(workout_name=workout_name)
    w_plan = workout_plan.objects.get(username=request.user.username, workout_name=workout_name)
    l = workout_level.objects.get(workout_name=w, level=w_plan.progress)
    
    if request.method == 'POST' and request.POST.get('button_clicked'):
        w_plan.progress += 1
        w_plan.save()
        show_button = w_plan.progress < 5
        return redirect('workoutprogression', workout_name=workout_name)
    
    show_button = w_plan.progress < 5
    return render(request, 'workoutprogression.html', {'w_plan': w_plan, 'w': w, 'w_level': l, 'show': show_button})
