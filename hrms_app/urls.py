from django.urls import path
from .views import add_employee, list_employees, delete_employee, mark_attendance, get_attendance , dashboard_counts,recent_employees 

urlpatterns = [
    path("employees/", list_employees),
    path("employees/add/", add_employee),
    path("employees/<str:emp_id>/", delete_employee),

    path("attendance/mark/", mark_attendance),
    path("attendance/<str:emp_id>/", get_attendance),
    path("dashboard/counts/", dashboard_counts),
    path("employees/recent/", recent_employees),
]
