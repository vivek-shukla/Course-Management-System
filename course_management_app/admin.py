from django.contrib import admin

from course_management_app.models import Course, StudentProfileInfo

# Register your models here.
admin.site.register(StudentProfileInfo)
admin.site.register(Course)
