"""
URL configuration for Clg_administration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1.views import Student_record,Faculty_record,Department_record,Home,C_student,C_faculty,C_dept,Admin_reg,Admin_login
urlpatterns = [
    path('admin/', admin.site.urls),
    path("std/",Student_record,name="students"),
    path("Fac/",Faculty_record,name="faculties"),
    path("dept",Department_record,name="departments"),
    path("hom/",Home,name="home_pge"),
    path("ljk/",C_student,name="stu_C"),
    path("kll/",C_faculty,name="fac_C"),
    path("low",C_dept,name="dept_C"),
    path("",Admin_reg,name="adm_regi"),
    path("lo/",Admin_login,name="kok")
   
    
]
