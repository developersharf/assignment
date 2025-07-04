from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=25)
    student_email = models.EmailField(max_length=29)
    batch = models.IntegerField()
    course = models.CharField(max_length=43)
    
    def __str__(self):
        return self.student_name
    
    
class Info(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=20)
    batch = models.IntegerField()
    password = models.CharField(max_length=35)
    re_password = models.CharField(max_length=35)
    textarea = models.CharField(max_length=150)