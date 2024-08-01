from django.db import models
from mongoengine import Document,fields


class user_details(Document):
    name=fields.StringField()
    dept=fields.StringField()
    username=fields.StringField()
    password=fields.StringField()
    status=fields.BooleanField(default=True)
    

class staff_details(Document):
    name=fields.StringField()
    dept=fields.StringField()
    username=fields.StringField()
    password=fields.StringField()
    status=fields.BooleanField(default=True)
    
    
    
class mark(Document):
    student_id=fields.StringField()
    staff_id=fields.StringField()
    semester=fields.StringField()
    mark1=fields.IntField()
    mark2=fields.IntField()
    mark3=fields.IntField()
    mark4=fields.IntField()
    status=fields.BooleanField(default=True)
    
    