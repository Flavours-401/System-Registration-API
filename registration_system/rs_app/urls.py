from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews
from .views import CustomUserList, CustomUserListDetail,AdminHODList,AdminHODListDetail,StaffsList,StaffsListDetail,CoursesDetail,CoursesList,SubjectsDetail,SubjectsList,StudentsDetail,StudentsList,AttendanceDetail,AttendanceList,AttendanceReportDetail,AttendanceReportList,LeaveReportStudentDetail,LeaveReportStudentList,LeaveReportStaffDetail,LeaveReportStaffList,FeedBackStudentDetail,FeedBackStudentList,FeedBackStaffsDetail,FeedBackStaffsList,NotificationStudentDetail,NotificationStudentList,NotificationStaffsDetail,NotificationStaffsList
    
urlpatterns = [
    path("v1/", CustomUserList.as_view(), name="_customUserList"),
    path("<int:pk>/", CustomUserListDetail.as_view(), name="CustomUserListDetail"),
   path("v1/", AdminHODList.as_view(), name="AdminHODList"),
    path("<int:pk>/", AdminHODListDetail.as_view(), name="AdminHODListDetail"),
       path("v1/", StaffsList.as_view(), name="StaffsList"),
    path("<int:pk>/", StaffsListDetail.as_view(), name="StaffsListDetail"),
       path("v1/", CoursesDetail.as_view(), name="CoursesDetail"),
    path("<int:pk>/", CoursesList.as_view(), name="CoursesList"),
       path("v1/", SubjectsDetail.as_view(), name="SubjectsDetail"),
    path("<int:pk>/", SubjectsList.as_view(), name="SubjectsList"),
       path("v1/", StudentsDetail.as_view(), name="StudentsDetail"),
    path("<int:pk>/", StudentsList.as_view(), name="StudentsList"),
       path("v1/", AttendanceDetail.as_view(), name="AttendanceDetail"),
    path("<int:pk>/", AttendanceList.as_view(), name="AttendanceList"),
       path("v1/", AttendanceReportDetail.as_view(), name="AttendanceReportDetail"),
    path("<int:pk>/", AttendanceReportList.as_view(), name="AttendanceReportList"),
       path("v1/", LeaveReportStudentDetail.as_view(), name="LeaveReportStudentDetail"),
    path("<int:pk>/", LeaveReportStudentList.as_view(), name="LeaveReportStudentList"),
     path("v1/", LeaveReportStaffDetail.as_view(), name="LeaveReportStaffDetail"),
    path("<int:pk>/", LeaveReportStaffList.as_view(), name="LeaveReportStaffList"),
     path("v1/", FeedBackStudentDetail.as_view(), name="FeedBackStudentDetail"),
    path("<int:pk>/", FeedBackStudentList.as_view(), name="FeedBackStudentList"),
     path("v1/", FeedBackStaffsDetail.as_view(), name="FeedBackStaffsDetail"),
    path("<int:pk>/", FeedBackStaffsList.as_view(), name="FeedBackStaffsList"),
     path("v1/", NotificationStudentDetail.as_view(), name="NotificationStudentDetail"),
    path("<int:pk>/", NotificationStudentList.as_view(), name="NotificationStudentList"),
     path("v1/", NotificationStaffsDetail.as_view(), name="NotificationStaffsDetail"),
    path("<int:pk>/", NotificationStaffsList.as_view(), name="NotificationStaffsList"),
    
]
