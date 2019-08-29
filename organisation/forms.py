from django import forms
from django.forms.models import inlineformset_factory
from .models import Student, Courses, Organisation

class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['name']

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name']

# OrganisationFormSet = inlineformset_factory( Organisation,Courses, form=CoursesForm,fields=['name',], extra=1, can_delete=True)       
   

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name',]



# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ( 'organisation', 'courses','name')

    
        