from django.contrib import admin
from .models import Student, Semester, CustomUser, Result, Issues_remarks, Academicyear, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'mentor']
    search_fields = ['id', 'name']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester_no', 'sgpa', 'student','backlogs']
    search_fields = ['id', 'student__name', 'semester_no','backlogs']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'uni_id', 'role','department']
    search_fields = ['username', 'email', 'uni_id','department']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'cgpa', 'tot_backlogs']
    search_fields = ['id', 'student__name','tot_backlogs']

@admin.register(Issues_remarks)
class IssuesRemarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'student', 'sem_id', 'mentor']
    search_fields = ['id', 'student__name', 'mentor__username']

@admin.register(Academicyear)
class AcademicyearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']
    search_fields = ['id', 'year']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'date_joined', 'attended', 'conducted', 'percentage']
    search_fields = ['id', 'student__name', 'date','percentage']
