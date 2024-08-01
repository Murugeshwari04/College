from . import views
from django.urls import path

app_name="student"
urlpatterns=[

    path('/student_login',views.student_login),
    path('/particular_display',views.particular_display),
    path('/all_sem_display',views.all_sem_display),
  
 
]
