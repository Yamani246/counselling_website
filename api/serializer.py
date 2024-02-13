from rest_framework import serializers
from .models import Student, Semester, CustomUser, Result, Issues_remarks, Academicyear, Attendance,Batch,Branch

class StudentSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.department') 
    batch_id=serializers.CharField(source='batch_id.batch_no')
    aca_year=serializers.CharField(source='aca_year.year')
    class Meta:
        model=Student
        fields='__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Semester
        fields='__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.department') 
    batch_id=serializers.CharField(source='batch_id.batch_no')
    class Meta:
        model=CustomUser
        fields='__all__'

class AcademicyearSerializer(serializers.ModelSerializer):
    class Meta:
        model=Academicyear
        fields='__all__'

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issues_remarks
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields='__all__'

class BatchSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.department') 
    aca_year=serializers.CharField(source='aca_year.year')
    class Meta:
        model=Batch
        fields='__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch 
        fields='__all__'