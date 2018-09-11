from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=25)
    assignment = models.CharField(max_length=100)

class StudentProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # user will have by default fields of User class
    course = models.OneToOneField(Course,on_delete=models.CASCADE)

    upload_assignment = models.FileField(blank=True)

    def __str__(self):
        return "%s %s"%(self.user.username,self.user.first_name)








# class Assignment(models.Model):
#     course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
#     assignment = models.CharField(max_length = 40)
#
#     def __str__(self):
#         return " %s "%(self.assignment)







# class Assignment(models.Model):
#     course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
#     assignment = {'publish':'','submission':[]}
#
#     def publish_assignment():
#         str = input("Enter Assignment :")
#         assignment['publish']=str
#     def submit_assignment():
#         user = input("Enter User name :")
#         message = input("Enter assignment :")
#         assignment['submission'].append((user,message))
