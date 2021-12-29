from django.urls import path
from courses_students.api import student_api_view, student_detail_view

urlpatterns = [
    path('students/', student_api_view, name='students_api' ),
    path('students/<int:pk>/', student_detail_view, name='student_detail_api')
]
