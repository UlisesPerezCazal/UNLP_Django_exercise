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