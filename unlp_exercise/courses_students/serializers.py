from django.db.models import fields
from rest_framework import serializers
from courses_students.models import Course, Student, Course_student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Course_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_student
        fields = '__all__'