from django.contrib import admin

from .models import Teacher, ClassTeacher, Subject, SubjectTeacher, Attendance, Marks

admin.site.register(Teacher)
admin.site.register(ClassTeacher)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)
admin.site.register(Attendance)
admin.site.register(Marks)
