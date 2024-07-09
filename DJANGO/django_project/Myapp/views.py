from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import PatientSignupForm, DoctorSignupForm
from .models import CustomUser

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'signup.html',{'form': form, 'user_type': 'Doctor'})

def doctor_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)

        if request.method == 'POST':
         form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Doctor'})

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
