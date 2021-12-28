from django.contrib import admin
from courses_students.models import Student, Course, Course_student
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Course_student)