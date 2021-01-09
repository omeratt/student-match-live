from django.contrib import admin
# from .models import Profile, Student
from .models import Student,Teacher,Report,Users_Report
# Register your models here.
# admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Report)
admin.site.register(Users_Report)
