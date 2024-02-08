
from rest_framework import generics
from .serializer import StudentSerializer,AcademicyearSerializer
from .models import Student,Academicyear
from rest_framework.permissions import AllowAny

class StudentListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class AcademicListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset=Academicyear.objects.all()
    
    serializer_class=AcademicyearSerializer