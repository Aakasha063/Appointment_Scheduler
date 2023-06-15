from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse

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
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')  # Redirect to the dashboard
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'accounts/home.html') 