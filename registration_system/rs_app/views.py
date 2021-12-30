# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.EmailBackEnd import EmailBackEnd
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs
from .permissions import IsOwnerOrReadOnly
from .serializer import student_management_Serializer
class CustomUserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = student_management_Serializer
class CustomUserListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = student_management_Serializer
class AdminHODList(ListCreateAPIView):
    queryset = AdminHOD.objects.all()
    serializer_class = student_management_Serializer
class AdminHODListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = AdminHOD.objects.all()
    serializer_class = student_management_Serializer
class StaffsList(ListCreateAPIView):
    queryset = Staffs.objects.all()
    serializer_class = student_management_Serializer
class StaffsListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Staffs.objects.all()
    serializer_class = student_management_Serializer
class CoursesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Courses.objects.all()
    serializer_class = student_management_Serializer
class CoursesList(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = student_management_Serializer
class SubjectsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Subjects.objects.all()
    serializer_class = student_management_Serializer
class SubjectsList(ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = student_management_Serializer
class StudentsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Students.objects.all()
    serializer_class = student_management_Serializer
class StudentsList(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = student_management_Serializer
class AttendanceDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Attendance.objects.all()
    serializer_class = student_management_Serializer
class AttendanceList(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = student_management_Serializer
class AttendanceReportDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = AttendanceReport.objects.all()
    serializer_class = student_management_Serializer
class AttendanceReportList(ListCreateAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = student_management_Serializer
class LeaveReportStudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = LeaveReportStudent.objects.all()
    serializer_class = student_management_Serializer
class LeaveReportStudentList(ListCreateAPIView):
    queryset =LeaveReportStudent.objects.all()
    serializer_class = student_management_Serializer
class LeaveReportStaffDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = LeaveReportStaff.objects.all()
    serializer_class = student_management_Serializer
class LeaveReportStaffList(ListCreateAPIView):
    queryset =LeaveReportStaff.objects.all()
    serializer_class = student_management_Serializer
class FeedBackStudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = FeedBackStudent.objects.all()
    serializer_class = student_management_Serializer
class FeedBackStudentList(ListCreateAPIView):
    queryset =FeedBackStudent.objects.all()
    serializer_class = student_management_Serializer
class FeedBackStaffsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = FeedBackStaffs.objects.all()
    serializer_class = student_management_Serializer
class FeedBackStaffsList(ListCreateAPIView):
    queryset =FeedBackStaffs.objects.all()
    serializer_class = student_management_Serializer
class NotificationStudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = NotificationStudent.objects.all()
    serializer_class = student_management_Serializer
class NotificationStudentList(ListCreateAPIView):
    queryset =NotificationStudent.objects.all()
    serializer_class = student_management_Serializer
class NotificationStaffsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = NotificationStaffs.objects.all()
    serializer_class = student_management_Serializer
class NotificationStaffsList(ListCreateAPIView):
    queryset =NotificationStaffs.objects.all()
    serializer_class = student_management_Serializer
