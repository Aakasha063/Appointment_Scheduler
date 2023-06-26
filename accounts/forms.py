from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class AppointmentForm(forms.Form):
    required_speciality = forms.CharField(max_length=100)
    date_of_appointment = forms.DateField(widget=AdminDateWidget())
    start_time_of_appointment = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'user_type')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('patient', 'Patient'), ('doctor', 'Doctor')))



