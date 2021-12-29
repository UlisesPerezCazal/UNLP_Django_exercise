from enum import unique
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.core.exceptions import ValidationError

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

    def __str__(self):
        return self.name
    
class Enrol(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    finalized = models.BooleanField(default=False)
    grade = models.PositiveSmallIntegerField(default=None, null=True, blank=True)

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        if self.finalized:
            return f"Alumno: {self.student.name} {self.student.last_name}, Curso: {self.course.name}, Nota: {self.grade}"
        return f"Alumno: {self.student.name} {self.student.last_name}, Curso: {self.course.name}, Finalized: {self.finalized}"

    def clean(self):
        if self.finalized is True and self.grade is None:
            raise ValidationError('Error: no se asignó la nota.')
        if self.finalized is False and self.grade is not None:
            raise ValidationError('Error: no se le puede asignar una nota si todavía no finalizó el curso.')
    