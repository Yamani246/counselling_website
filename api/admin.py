from django.contrib import admin
from .models import Student, Semester, CustomUser, Result, Issues_remarks, Academicyear, Attendance,Batch,Branch

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department','batch_id']
    search_fields = ['id', 'name']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester_no']
    search_fields = ['id','semester_no']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'uni_id', 'role','department']
    search_fields = ['username', 'email', 'uni_id','department']

admin.site.register(Result)
admin.site.register(Branch)

@admin.register(Issues_remarks)
class IssuesRemarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'sem_id']
    search_fields = ['id', 'student__name', 'mentor__username']

@admin.register(Academicyear)
class AcademicyearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']
    search_fields = ['id', 'year']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'date', 'attended', 'conducted', 'percentage']
    search_fields = ['id', 'student__name', 'date','percentage']

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display=['id','batch_no']