from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from app1.models import Student,Faculty,Department
from app1.forms import new_stu,new_fac,new_dep
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def Home(request):
    return render(request,'Home/Home_page.html')



def Student_record(request):
    data=Student.objects.all()
    context={
        'data':data
    }
    return render(request,'records/Student_rec.html',context)


def  Faculty_record(request):
    data=Faculty.objects.all()
    context={
        'data':data

    }
    return render(request,'records/Faculty_rec.html',context)

def Department_record(request):
    data=Department.objects.all()
    context={
        'data':data
    }
    return render(request,'records/Dept_rec.html',context)



def C_student(request):
    form=new_stu()
    if request.method=="POST":
        form=new_stu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

    context={
        'form':form
    }



    return render(request,'formss/stu_form.html',context)

def C_faculty(request):
    form=new_fac()
    if request.method=="POST":
        form=new_fac(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculties')

    context={
        'form':form
    }


    return render(request,'formss/fac_form.html',context)



def C_dept(request):
    form=new_dep()
    if request.method=="POST":
        form=new_dep(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')

    context={
        'form':form
    }


    return render(request,'formss/Dept_form.html',context)



#authentication


def Admin_reg(request):
    message=" "
    if request.method=="POST":
        username1=request.POST.get('uname')
        Email1=request.POST.get('uemail')
        password1=request.POST.get('upassword')
        p2=request.POST.get('uconpassword')

        if password1!=p2:
            message=" Two passwords are not matching"
        elif User.objects.filter(email=Email1).exists():
            message="The user already exists"
        else:
            user=User.objects.create_user(username=username1,email=Email1,password=password1)
            user.save()
            return redirect('home_pge')
        


    return render(request,'Auth/Registration.html',{
            'message':message
        })


def Admin_login(request):
    message=" "
    if request.method=="POST":
        username1=request.POST.get('uname')
        
        password1=request.POST.get('upassword')
        user=authenticate(request,username=username1,password=password1)
        if user is not None:
            login(request,user)
            return redirect('home_pge')
        else:
            message="invalid credentials"
    
       

        


    return render(request,'Auth/login_user.html',{
            'message':message
        })