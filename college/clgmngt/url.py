from ..college import views
from django.urls import path


app_name='myapp'
urlpatterns=[
        path('/user',views.user_register),    
        path('/sample',views.sample),
        path('/mail',views.mail),
       
]