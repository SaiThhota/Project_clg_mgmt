from django.db import models



# Create your models here.
class Student(models.Model):
    Std_id=models.IntegerField(unique=True)
    Std_name=models.CharField(max_length=50)
    Std_Email=models.EmailField()
    Std_Age=models.BigIntegerField()
    Std_year=models.IntegerField()
    Std_place=models.CharField(max_length=50)



class Faculty(models.Model):
    Fac_id=models.IntegerField(unique=True)
    Fac_name=models.CharField(max_length=50)
    Fac_Email=models.EmailField()
    Fac_Mobile=models.BigIntegerField()
    depart=[
        ('cse','CSE'),
        ('mech','MECH'),
        ('eee','EEE'),
        ('civil','CIVIL'),
        ('ece','ECE'),
        ('it','IT')    ]
    Fac_dept=models.CharField(max_length=50,choices=depart)


class Department(models.Model):
    Dept_id=models.IntegerField(unique=True)
    Dept_name=models.CharField(max_length=50)
    Dept_code=models.IntegerField()
