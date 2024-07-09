from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class PatientSignupForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user