from django.contrib import admin
from app.models import Student, Course, Enrollment


class Students(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "rg",
        "cpf",
        "birth_date",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 20


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "description",
    )
    list_display_links = ("code",)
    list_per_page = 5


admin.site.register(Course, Courses)


class Enrollments(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
        "period",
    )
    list_display_links = ("id",)


admin.site.register(Enrollment, Enrollments)
