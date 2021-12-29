from django.urls import path
from courses_students.api import student_api_view, student_detail_view, courses_api_view, course_detail_view

urlpatterns = [
    path('students/', student_api_view, name='students_api' ),
    path('students/<int:pk>/', student_detail_view, name='student_detail_api'),
    path('courses/', courses_api_view, name='courses_api'),
    path('courses/<int:pk>/', course_detail_view, name='course_detail_api')
]
