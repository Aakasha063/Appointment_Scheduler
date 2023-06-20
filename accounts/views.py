from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from .models import Patient, Doctor
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def patient_dashboard(request):
    # Logic for the patient dashboard
    return render(request, 'accounts/patient_dashboard.html')

def doctor_dashboard(request):
    # Logic for the doctor dashboard
    return render(request, 'accounts/doctor_dashboard.html')

def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'accounts/home.html') 


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                # Passwords don't match, handle the error
                return HttpResponse("Passwords do not match")
            user = form.save()
            user_type = form.cleaned_data['user_type']
            if user_type == 'P':
                Patient.objects.create(user=user)
                login(request, user)
                messages.success(request, 'Account created successfully')
                return redirect('accounts:patient_dashboard')
            elif user_type == 'D':
                Doctor.objects.create(user=user)
                login(request, user)
                messages.success(request, 'Account created successfully')
                return redirect('accounts:doctor_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            # Authenticate user based on username and password
            user = authenticate(username=username, password=password)

            if user is not None:
                # Check if the authenticated user is of the correct user type
                if user_type == 'patient' and hasattr(user, 'patient'):
                    # Logic for patient login
                    login(request, user)
                    return redirect('accounts:patient_dashboard')
                elif user_type == 'doctor' and hasattr(user, 'doctor'):
                    # Logic for doctor login
                    login(request, user)
                    return redirect('accounts:doctor_dashboard')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


