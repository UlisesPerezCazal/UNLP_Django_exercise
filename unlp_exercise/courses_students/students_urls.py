from django.urls import path
from courses_students.api import student_api_view, student_detail_view, average_grade_view 

urlpatterns = [
    path('', student_api_view, name='students_api' ),
    path('<int:pk>/', student_detail_view, name='student_detail_api'),
    path('<int:pk>/average/', average_grade_view, name='student_average_api'), 
]
