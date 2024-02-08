
from django.urls import path
from . import views
urlpatterns = [
    path('academic_list/',views.AcademicListView.as_view()),
]
