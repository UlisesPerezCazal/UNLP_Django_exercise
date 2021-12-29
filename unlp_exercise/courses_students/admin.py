from django.contrib import admin
from courses_students.models import Student, Course, Enrol
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrol)