from enum import unique
from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    students = ManyToManyField(Student, through='Course_student')

    def __str__(self):
        return self.name
    
class Course_student(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.SmallIntegerField()

    class Meta:
        unique_together = [['student', 'course']]