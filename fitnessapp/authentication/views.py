from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from .models import workout
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
    return render(request, 'profile.html', {'username':username,'email':email})

def workouts(request):
    workout_list= workout.objects.all()
    return render(request, "workouts.html", {'workout_list': workout_list})
