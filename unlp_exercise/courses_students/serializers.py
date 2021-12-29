from django.db.models import fields
from rest_framework import serializers
from courses_students.models import Course, Student, Enrol

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrol
        fields = '__all__'

class AverageSerializer(serializers.Serializer):
    average = serializers.FloatField()