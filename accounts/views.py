from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, AppointmentForm
from .models import Patient, Doctor
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import create_calendar_event, calculate_end_time


def appointment_confirmation(request):
    return render(request, 'accounts/appointment_confirmation.html')

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            required_speciality = form.cleaned_data['required_speciality']
            date_of_appointment = form.cleaned_data['date_of_appointment']
            start_time_of_appointment = form.cleaned_data['start_time_of_appointment']
            end_time_of_appointment = calculate_end_time(start_time_of_appointment)
            create_calendar_event(doctor, date_of_appointment, start_time_of_appointment, end_time_of_appointment, required_speciality)
            
            return render(request, 'accounts/appointment_confirmation.html', {
                'doctor': doctor,
                'required_speciality': required_speciality,
                'date_of_appointment': date_of_appointment,
                'start_time_of_appointment': start_time_of_appointment,
                'end_time_of_appointment': end_time_of_appointment,
            })
    else:
        form = AppointmentForm()

    return render(request, 'accounts/book_appointment.html', {'form': form, 'doctor': doctor, 'doctor_id': doctor_id})

def patient_dashboard(request):
    doctors = Doctor.objects.select_related('user').all()
    return render(request, 'accounts/patient_dashboard.html', {'doctors': doctors})

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


