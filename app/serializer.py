from dataclasses import fields
from imp import source_from_cache
from rest_framework import serializers
from app.models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "rg", "cpf", "birth_date"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"


class ListEnrollmentStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()


class ListEnrollmentCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = Enrollment
        fields = ["student_name"]
