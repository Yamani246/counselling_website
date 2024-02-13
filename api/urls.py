
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('academic/create/',views.AcademicCreateListView.as_view()),
    path('academic/<int:pk>', views.AcademicDetailsUpdateDestoryView.as_view()),
    path('attendance/create/',views.AttendanceCreateView.as_view()),
    path("batch/create/", views.BatchCreateListView.as_view()),
    path('batch/<int:pk>/',views.BatchDetailsUpdateDestoryView.as_view()),
    path('branch/create/',views.BranchCreateListView.as_view()),
    path('issues/create/',views.IssuesCreateView.as_view()),
    path('token/', obtain_auth_token, name='obtain_token'),
    path('logout/',views.LogoutView.as_view()),
    path('report/',views.ReportView.as_view()),
    path('result/create/',views.ResultCreateView.as_view()),
    path('result/<int:pk>/',views.ResultRetrieveUpdateView.as_view()),
    path('semester/create/',views.SemesterCreteView.as_view()),
    path('student/create/',views.StudentCreateView.as_view()),
    path('student/update/<int:pk>/',views.StudentRetrieveUpdateView.as_view()),
    path('student/details/',views.StudentDetailView.as_view()),
    path('student/delete/<int:pk>/',views.StudentDeleteView.as_view()),
    path('student/list/',views.StudentListView.as_view()),
    path('user/create/',views.UserCreateView.as_view()),
    path('user/update/<int:pk>/',views.UserRetrieveUpdateView.as_view()),
    path('user/delete/<int:pk>/',views.UserDeleteView.as_view()),
    path('user/list/',views.UserListView.as_view()),
]
