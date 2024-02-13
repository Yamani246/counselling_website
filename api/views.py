from rest_framework import generics
from .serializer import StudentSerializer,AcademicyearSerializer,CustomUserSerializer,ResultSerializer,BatchSerializer,BranchSerializer,AttendanceSerializer,SemesterSerializer,IssuesSerializer
from .models import Student,Academicyear
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Semester, CustomUser, Issues_remarks, Academicyear, Attendance,Batch,Branch,Result
from .permissions import IsAdminUserOrReadOnly,IsHodAdmin
from django.contrib.auth import logout
from rest_framework import status

class AcademicCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset=Academicyear.objects.all()
    serializer_class=AcademicyearSerializer

class AcademicDetailsUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset=Academicyear.objects.all()
    serializer_class=AcademicyearSerializer

class AttendanceCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

class BatchCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly,IsAuthenticated]
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer

class BatchDetailsUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsHodAdmin,IsAuthenticated]
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer

class BranchCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer

class IssuesCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Issues_remarks.objects.all()
    serializer_class=IssuesSerializer

class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class ReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        id=request.query_params.get('id', None)
        sem_no=request.query_params.get('semester', None)
        result=Result.objects.filter(student=id)
        attendance=Attendance.objects.filter(student=id,sem_id=sem_no)
        issues=Issues_remarks.objects.filter(student=id,sem_id=sem_no)
        serializer_result=ResultSerializer(result,many=True)
        serializer_attendence = AttendanceSerializer(attendance,many=True)
        serializer_issues = IssuesSerializer(issues,many=True)
        serializer={
            'Result':serializer_result.data,
            'attendence':serializer_attendence.data,
            'issues':serializer_issues.data
        }
        return Response(serializer)

class ResultCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Result.objects.all()
    serializer_class=ResultSerializer

class ResultRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Result.objects.all()
    serializer_class=ResultSerializer
    lookup_field='pk'

class SemesterCreteView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Semester.objects.all()
    serializer_class=SemesterSerializer


class StudentCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly,IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        password = validated_data.get('password')
        if password:
            student_instance = serializer.save()
            student_instance.set_password(password)
            student_instance.save()


class StudentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field='pk'

class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        id= request.query_params.get('id', None)
        serializer_semester=Semester.objects.all()
        serializer_student=Student.objects.get(id=id)
        serializer={
            'student':serializer_student.data,
            'semester':serializer_semester.data
        }
        return Response(serializer)
    
class StudentDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAdminUserOrReadOnly,IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == 'principal' or user.role=='admin':
            academicyear = request.query_params.get('academicyear')
            branch = request.query_params.get('branch', None)
            queryset = Student.objects.filter(department=branch, aca_year__id=academicyear)
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)

        elif user.role == 'hod':
            mentor_id= request.query_params.get('id', None)
            mentor_details=CustomUser.objects.get(pk=mentor_id)
            queryset = Student.objects.filter(batch_id=mentor_details.batch_id)
            serializer_mentor=CustomUserSerializer(mentor_details)
            serializer_student = StudentSerializer(queryset, many=True)
            serializer={
                'student':serializer_student.data,
                'mentor':serializer_mentor.data
            }
            return Response(serializer)
        
        elif user.role=='counsellor':
            batch = user.batch_id
            queryset = Student.objects.filter(batch_id=batch)
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)
        
        return Response('Cannot access data with your credentials')
        

class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly,IsAuthenticated]
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        password = validated_data.get('password')
        if password:
            student_instance = serializer.save()
            student_instance.set_password(password)
            student_instance.save()


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsHodAdmin,IsAuthenticated]
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
        instance=serializer.instance
        updated_password=self.request.data.get('password')
        if updated_password:
            instance.set_password(updated_password)
        serializer.save()


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly,IsAuthenticated]
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer

class UserListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        print(user)
        if user.role=='hod':
            queryset=CustomUser.objects.filter(department=user.department)
            serializer=CustomUserSerializer(queryset,many=True)
            return Response(serializer.data)

        elif user.role=='admin' or user.role=='principal':
            branch = request.query_params.get('branch', None)
            branch=Branch.objects.get(department=branch)
            queryset=CustomUser.objects.filter(department=branch)
            serializer=CustomUserSerializer(queryset,many=True)
            return Response(serializer.data)
        
        else:
            return Response('You cannot access these details')
        