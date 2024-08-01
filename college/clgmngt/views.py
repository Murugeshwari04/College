from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *


@api_view(['POST'])
def student_login(request):
    data=request.data
    username=request.data['email']
    password=request.data['password']
    user_data=user_details.objects.filter(username=username).first()
    if user_data:
        print(user_data.password)
        if user_data.password != password:
           output="Password is incorrect"
        else:
            output='login successfully'
        
    else:
            output="Email is incorrect"
        
    return Response(output)

@api_view(['GET'])
def particular_display(request):
    username=request.query_params.get('email')
    password=request.query_params.get('password')
    user_data=user_details.objects.filter(username=username,password=password).first()
    if user_data:
        marks={
           'Name':user_data.name,
           'percentage':0,
           'semester_list':[]
            }
        student=mark.objects.filter(student_id=str(user_data.id)).first()
        print(student)
        
        sem={
            'Sem':student.semester,
            'mark1':student.mark1,
            'mark2':student.mark2,
            'mark3':student.mark3,
            'mark4':student.mark4,
            
            }
        marks['semester_list'].append(sem)
        percentage=((student.mark1+student.mark2+student.mark3+student.mark4)/400)*100
        marks['percentage']=percentage
        print(percentage)
        
    else:
        return Response("User is not permited")
            
    return Response(marks)   




     





@api_view(['GET'])
def all_sem_display(request):
    username=request.query_params.get('email')
    password=request.query_params.get('password')
    user_data=user_details.objects.filter(username=username,password=password).first()
    if user_data:
        marks={
           'Name':user_data.name,
           'percentage':0,
           'semester_list':[]
            }
        student=mark.objects.filter(student_id=str(user_data.id))
        print(student)
        per=0
        for i in student:
        
            sem={
                'Semester':i.semester, 
                'mark1':i.mark1,
                'mark2':i.mark2,
                'mark3':i.mark3,
                'mark4':i.mark4,
                
                }
            marks['semester_list'].append(sem)
            per +=((i.mark1+i.mark2+i.mark3+i.mark4)/400)*100
        marks['percentage']=(per/len(marks['semester_list']))
       
    else:
        return Response("User is not permited")
            
    return Response(marks)   




     





