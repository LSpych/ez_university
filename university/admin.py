from django.contrib import admin
from .models import Semester, Course, Instructor, Student

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
