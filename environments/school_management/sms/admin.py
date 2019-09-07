from django.contrib import admin

from .models import Teacher, ClassTeacher, Subject, SubjectTeacher

admin.site.register(Teacher)
admin.site.register(ClassTeacher)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)
