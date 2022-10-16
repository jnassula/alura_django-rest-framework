from rest_framework import viewsets, generics
from app.models import Enrollment, Student, Course
from app.serializer import (
    EnrollmentSerializer,
    StudentSerializer,
    CourseSerializer,
    ListEnrollmentStudentSerializer,
    ListEnrollmentCourseSerializer,
)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Alunos"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticated


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Matriculas"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticated


class ListEnrollmentStudent(generics.ListAPIView):
    """Exibindo a lista de alunos matriculados"""

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListEnrollmentStudentSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticated


class ListEnrollmentCourse(generics.ListAPIView):
    """Exibindo lista de alunos matriculados num curso especifico"""

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListEnrollmentCourseSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticated
