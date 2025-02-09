"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/patient/',views.patient_signup ),
    path('signup/doctor/', views.doctor_signup),
    path('login/', views.login_view),
    path('dashboard/patient/', views.patient_dashboard),
    path('dashboard/doctor/', views.doctor_dashboard),
   
]

"""
from Myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/patient/',views.patient_signup ),
    path('signup/doctor/', views.doctor_signup),
    path('login/', views.login_view),
    path('dashboard/patient/', views.patient_dashboard),
    path('dashboard/doctor/', views.doctor_dashboard),
]"""