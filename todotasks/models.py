from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length= 200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    