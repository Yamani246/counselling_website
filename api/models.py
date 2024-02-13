from django.db import models
from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='')
    email = models.EmailField(unique=True, default='')
    uni_id = models.CharField(max_length=50)
    role = models.CharField(max_length=50,null=True)
    department=models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True,related_name='user_branch')
    batch_id=models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, blank=True,related_name='batch_m')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'  

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Academicyear(models.Model):
    id = models.AutoField(primary_key=True)
    year=models.CharField(max_length=100)

    def __str__(self):
        return f'year {self.year}'

class Batch(models.Model):
    id=models.AutoField(primary_key=True)
    batch_no=models.CharField(max_length=100)
    no_of_students=models.IntegerField(null=True, blank=True)
    from_roll=models.CharField(max_length=50,null=True, blank=True)
    to_roll=models.CharField(max_length=50,null=True, blank=True)
    department=models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True,related_name='batch_branch')
    aca_year=models.ForeignKey('Academicyear', on_delete=models.CASCADE, null=True, blank=True,related_name='batch_academic_year')
    def __str__(self):
        return f'batch no {str(self.batch_no)}'
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    reg_id=models.CharField(max_length=50)
    batch_id=models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, blank=True,related_name='batch_s')
    aca_year=models.ForeignKey('Academicyear', on_delete=models.CASCADE, null=True, blank=True,related_name='student')
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=50,default='',null=True,blank=True)
    department=models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True,related_name='student_branch')
    section=models.CharField(max_length=50,default='',null=True,blank=True)
    dob=models.DateField(default=None)
    mother_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    guardian=models.CharField(max_length=100)
    mother_occupation=models.CharField(max_length=100)
    father_occupation=models.CharField(max_length=100)
    permanent_add=models.CharField(max_length=1000)
    present_add=models.CharField(max_length=1000)
    transport=models.CharField(max_length=100)
    hostler=models.CharField(max_length=100,default='')
    ten_board=models.CharField(max_length=100)
    ten_school=models.CharField(max_length=100)
    ten_cgpa=models.DecimalField(max_digits=10, decimal_places=2)
    inter_board=models.CharField(max_length=100)
    inter_clg=models.CharField(max_length=100)
    inter_cgpa=models.DecimalField(max_digits=10, decimal_places=2)
    diplomo_board=models.CharField(max_length=100)
    diplomo_clg=models.CharField(max_length=100)
    dimplomo_cgpa=models.DecimalField(max_digits=10, decimal_places=2)
    quota=models.CharField(max_length=100)
    ecet_eamcet_rank=models.IntegerField()
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    cgpa=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    tot_backlogs=models.IntegerField( null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.id}"

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    sem_id=models.ForeignKey('Semester', on_delete=models.CASCADE, null=True, blank=True,related_name='sem_attendance')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True,related_name='attendances')
    date = models.DateTimeField(default=timezone.now)
    attended=models.IntegerField()
    conducted=models.IntegerField()
    percentage=models.DecimalField(max_digits=10, decimal_places=2)
    reasons=models.CharField(max_length=100)
    medical_certificate=models.CharField(max_length=100)
    
    def __str__(self):
        return f"Attendance - {self.id} (Student: {self.student.name if self.student else 'No Student'})"

class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    semester_no=models.IntegerField()
    def __str__(self):
        return str(self.semester_no)
    
class Result(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True,related_name='result')
    sem_id=models.ForeignKey('Semester', on_delete=models.CASCADE, null=True, blank=True,related_name='result_sem')
    sgpa=models.DecimalField(max_digits=10, decimal_places=2)
    backlogs = models.PositiveIntegerField(default=0)
    backlog_list = models.TextField(blank=True)

    
class Issues_remarks(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True,related_name='issue_student')
    sem_id=models.ForeignKey('Semester', on_delete=models.CASCADE, null=True, blank=True,related_name='issue_sem')
    mentor = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True,related_name='counsellor_issue')
    remark=models.TextField(blank=True)
    economic=models.TextField(blank=True)
    family=models.TextField(blank=True)
    teenage=models.TextField(blank=True)
    health=models.TextField(blank=True)
    emotional=models.TextField(blank=True)
    psychological=models.TextField(blank=True)
    Additional=models.TextField(blank=True)

    def __str__(self):
        return f"IssuesRemarks - {self.date} ({self.student.name if self.student else 'No Student'})"

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.department