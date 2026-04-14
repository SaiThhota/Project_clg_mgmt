from django.contrib import admin


# Register your models here.
from app1.models import Student,Department,Faculty


class Admin_student(admin.ModelAdmin):
    list_display=['Std_id','Std_name','Std_Email','Std_Age','Std_year','Std_place']

admin.site.register(Student,Admin_student)


class Admin_Falculty(admin.ModelAdmin):
    list_display=['Fac_id','Fac_name','Fac_Email','Fac_Mobile','Fac_dept']
admin.site.register(Faculty,Admin_Falculty)   

class Admin_Department(admin.ModelAdmin):
    list_display=['Dept_id','Dept_name','Dept_code']
admin.site.register(Department,Admin_Department)