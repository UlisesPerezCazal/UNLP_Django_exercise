from django.db.models.fields import GenericIPAddressField
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.utils import serializer_helpers
from courses_students.models import Course, Student, Enrol
from courses_students.serializers import StudentSerializer, CourseSerializer, EnrolSerializer, AverageSerializer
import csv

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

@api_view(['GET'])
def average_grade_view(request, pk):
    if request.method == 'GET':
        student = Student.objects.get(id = pk)
        enrol_list = Enrol.objects.filter(student = student.id)
        grades = 0
        average = None
        for i in range(len(enrol_list)):
            grades += enrol_list[i].grade
        if len(enrol_list) != 0:
            average = {'average': grades/len(enrol_list)}
            average_serializer = AverageSerializer(data = average)
            if average_serializer.is_valid():
                return Response(average_serializer.data)
            #return Response(f"El alumno {student.name} {student.last_name} tiene un prmedio de {average_serializer}")
        return JsonResponse({'Message': 'No hay suficientes cursos'}, status=404)

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
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)

    elif request.method == 'DELETE':
        course = Course.objects.get(id = pk)
        course.delete()
        return Response("Curso eliminado")

@api_view(['GET' ,'POST', 'PUT'])
def enrol_student_view(request):
    if request.method == 'POST':
        enrol_serializer = EnrolSerializer(data=request.data)
        if enrol_serializer.is_valid():
            enrol_serializer.save()
            return Response(enrol_serializer.data)
        return Response(enrol_serializer.errors)

    elif request.method == 'PUT':
        student_id = request.data.get('student')
        course_id = request.data.get('course')
        if course_id and student_id:
            course = Course.objects.get(id = course_id)
            student = Student.objects.get(id = student_id)
            enrol = Enrol.objects.get(student = student, course = course)
            enrol_serializer = EnrolSerializer(enrol, data=request.data)
            if enrol_serializer.is_valid():
                enrol_serializer.save()
                return Response(enrol_serializer.data)
            return Response(enrol_serializer.errors)
        return JsonResponse({'Message': 'El curso y el estudiante son requeridos'}, status=400)

    elif request.method == 'GET':
        enroll = Enrol.objects.all()
        enroll_serializer = EnrolSerializer(enroll, many=True)
        return Response(enroll_serializer.data)
    
@api_view(['GET'])
def course_students_view(request, pk):
    if request.method == 'GET':
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = 'atachment; filename="student.csv"'
        writer = csv.writer(response)
        writer.writerow(['Curso', 'Estudiante', 'Finalizado', 'Nota'])
        students = Enrol.objects.filter(course=pk)
        for student in students:
            writer.writerow([student.course.name, student.student.name, student.finalized, student.grade])
        return response