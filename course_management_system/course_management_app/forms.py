from django import forms
from django.contrib.auth.models import User
from course_management_app.models import StudentProfileInfo,Course


# class UserForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = "__all__"

class StudentProfileInfoForm(forms.ModelForm):
    class Meta():
        model = StudentProfileInfo
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = '__all__'

# class AssignmentForm(forms.ModelForm):
#     class Meta():
#         model = Assignment
#         fields = '__all__'
