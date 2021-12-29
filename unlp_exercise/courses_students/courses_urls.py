from django.urls import path
from courses_students.api import courses_api_view, course_detail_view

urlpatterns = [
    path('', courses_api_view, name='courses_api'),
    path('<int:pk>/', course_detail_view, name='course_detail_api')
]