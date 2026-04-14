from django import forms
from app1.models import Student,Faculty,Department
class new_stu(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class new_fac(forms.ModelForm):
    class Meta:
        model=Faculty
        fields='__all__'

        
class new_dep(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'