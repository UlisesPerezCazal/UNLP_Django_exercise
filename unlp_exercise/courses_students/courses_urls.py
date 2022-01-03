from django.urls import path
from courses_students.api import courses_api_view, course_detail_view, enrol_student_view, course_students_view

urlpatterns = [
    path('', courses_api_view, name='courses_api'),
    path('<int:pk>/', course_detail_view, name='course_detail_api'),
    path('<int:pk>/students/', course_students_view, name='course_students_api'),
    # A nivel RESTful podriamos especificar de forma mas semantica el endpoint de enrolamientos
    # teniendo como base un curso especifico.
    # Por ejemplo: 
    # CREAR y LISTAR > .../courses/<COURSE_ID>/enrollments/
    # DETALLE, MODIFICACION y ELIMINACION > .../courses/<COURSE_ID>/enrollments/ENROLLMENT_ID/
    path('enrol/', enrol_student_view, name='enrol_student_api'),
]