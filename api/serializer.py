from rest_framework import serializers
from .models import Student, Semester, CustomUser, Result, Issues_remarks, Academicyear, Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Semester
        fields='__all__'

class CustomUserSerializer(serializers.ModelSerializer):
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