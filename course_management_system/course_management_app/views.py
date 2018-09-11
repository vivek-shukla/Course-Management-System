from django.shortcuts import render
from course_management_app.forms import StudentProfileInfoForm , CourseForm

def index(request):
    return render(request,'course_management_app/index.html')

# Create your views here.

def userdetails(request):
    stude_form = StudentProfileInfoForm()
    course_form = CourseForm()
    # assignment_form = AssignmentForm()

    return render(request,'course_management_app/user.html',{'stude_form':stude_form,'course_form':course_form,})
