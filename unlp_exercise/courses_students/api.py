from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.utils import serializer_helpers
from courses_students.models import Course, Student, Course_student
from courses_students.serializers import StudentSerializer, CourseSerializer, Course_studentSerializer

@api_view(['GET', 'POST'])
def student_api_view(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)
    
    elif request.method == 'POST':
        students_serializer = StudentSerializer(data = request.data)
        if students_serializer.is_valid():
            students_serializer.save()
            return Response(students_serializer.data)
        return Response(students_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_view(request, pk):
    if request.method == 'GET':
        student = Student.objects.get(id = pk)
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)
    
    elif request.method == 'PUT':
        student = Student.objects.get(id = pk)
        student_serializer = StudentSerializer(student, data = request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        return Response(student_serializer.errors)

    elif request.method == 'DELETE':
        student = Student.objects.get(id = pk)
        student.delete()
        return Response("Estudiante eliminado")

@api_view(['GET', 'POST'])
def courses_api_view(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courses_serializer = CourseSerializer(courses, many=True)
        return Response(courses_serializer.data)
    
    elif request.method == 'POST':
        courses_serializer = CourseSerializer(data = request.data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return Response(courses_serializer.data)
        return Response(courses_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail_view(request, pk):
    if request.method == 'GET':
        course = Course.objects.get(id = pk)
        course_serializer = CourseSerializer(course)
        return Response(course_serializer.data)
    
    elif request.method == 'PUT':
        course = Course.objects.get(id = pk)
        course_serializer = CourseSerializer(course, data = request.data)
        student = Student.objects.get(id = pk)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)

    elif request.method == 'DELETE':
        course = Course.objects.get(id = pk)
        course.delete()
        return Response("Curso eliminado")