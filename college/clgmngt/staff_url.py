from . import staff
from django.urls import path

app_name="Staff"

urlpatterns=[
    path('/staffregister',staff.staff_register),
    path('/stafflogin',staff.staff_login),
    path('/student_register',staff.student_register),
    path('/mark',staff.add_mark),
    path('/student_list',staff.student_list),
    path('/edit_markentry',staff.edit_markentry),
    path('/delete_markentry',staff.delete_markentry),
    path('/delete_student',staff.delete_student),
    path('/status_updated',staff.status_updated),


   
]