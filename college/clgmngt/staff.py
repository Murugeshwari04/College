from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .utills1.jwt import*

@api_view(['POST'])
def staff_register(request):
    data=request.data
    staffid=staff_details.objects.filter(username=data['email'])
    if staffid:
         return Response("Email Already exists")
    user=staff_details(
        name=data['name'],
        dept=data['dept'],
        username=data['email'],
        password=data['password'],
       
    )

    user.save()
    
    return Response("Registered successfully")

@api_view(['POST'])
def staff_login(request):
    data=request.data
    username=request.data['email']
    password=request.data['password']
    user_data=staff_details.objects.filter(username=username).first()
    if user_data:
        print(user_data.password)
        if user_data.password != password:
           output="Password is incorrect"
        else:
            us={
                'id':str(user_data.id),
                'name':user_data.name
            }
            output=jwtencode(us)
    else:
            output="Email is incorrect"
        
    return Response(output)


@api_view(['POST'])
def student_register(request):
    data=request.data
    username=request.data['email']
    user=staff_details.objects.filter(username=username).first()
    if user:
        student=user_details.objects.filter(username=data['gmail']).first()
        if student:
            return Response("Already exists")
        student=user_details(
            name=data['name'],
            dept=data['dept'],
            username=data['gmail'],
            password=data['password'],
        )
        student.save()
    return Response("Registered successfully")

@api_view(['POST'])
@jwt_required
def add_mark(request):
    data = request.data
    se=request.decoded_token
    
   
    user_data = staff_details.objects.filter(id=se['id']).first()
    if  user_data :
        student=user_details.objects.filter(id=data['id']).first()
        if student:
            new_mark = mark(
                staff_id=str(user_data.id),
                student_id=str(student.id),
                semester=request.data['semester'],
                mark1=data['mark1'],
                mark2=data['mark2'],
                mark3=data['mark3'],
                mark4=data['mark4'],
            )
            new_mark.save()
            return Response("mark enterd successfully")
        else:
         return Response("staffid is invalid")
    else:
        return Response("staff id is invalid")
    

        
@api_view(['GET'])
@jwt_required
def student_list(request):
    data=request.decoded_token['id']

    user=staff_details.objects.filter(id=data).first()
    output=[]

    if user:
        data1=user_details.objects.filter(dept=user.dept)
        if data1:
            for i in data1:
                stu={'id':str(i.id),'name':i.name,'dept':i.dept,'email':i.username}

                output.append(stu)
        else:
            return("Failed")
        
@api_view(['PATCH'])
@jwt_required
def edit_markentry(request):
    data=request.data
    data_t=request.decoded_token
    user_data=staff_details.objects.filter(id=data_t['id']).first()
    if user_data:
        student=user_details.objects.filter(id=data['student_id']).first()
        if student:
            
            student_mark = {
               
                'semester':request.data['semester'],
                'mark1':data['mark1'],
                'mark2':data['mark2'],
                'mark3':data['mark3'],
                'mark4':data['mark4'],
                
               
            }
            mark.objects.filter(id=data['mark_id']).update(**student_mark )
            return Response("Student mark is updated successfully")
        
        else:
            return Response("Student ID is not valid")
    
    else:
        return Response("Staff is not permitted")
                
        
    return Response(output) 

@api_view(['PATCH'])
@jwt_required
def delete_markentry(request):
    data=request.data
    data_t=request.decoded_token
    user_data=staff_details.objects.filter(id=data_t['id']).first()
    if user_data:
        
            mark.objects.filter(id=data['mark_id']).delete()
            return Response("Student mark is deleted successfully")
        

    else:
        return Response("User is not permitted")



@api_view(['PATCH'])
@jwt_required
def delete_student(request):
    data=request.data
    data_t=request.decoded_token
    user_data=staff_details.objects.filter(id=data_t['id']).first()
    if user_data:
        
        user_details.objects.filter(id=data['student_id']).update(status=False)
        return Response("Student is deleted successfully")
        

    else:
        return Response("User is not permitted")
        
@api_view(['PATCH'])
def status_updated(request):
    staff_details.objects.all().update(status=True)
    return Response("Updated")
