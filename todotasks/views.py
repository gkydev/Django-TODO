from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import * 
import json
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request, "home.html")

@login_required(login_url="/login")
def home(request):
    my_lists = ToDoList.objects.filter(user_id=request.user.id)
    data = {}
    for my_list in my_lists:
        list_tasks = Task.objects.filter(todolist_id=my_list.id)
        data[my_list] = list_tasks 
    context = {
        "lists" : data,
        "form" : TaskForm()
    }
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            chosen_list = ToDoList.objects.get(id=int(request.POST.get('list_id')))
            form.instance.todolist = chosen_list
            form.save()
        return redirect('/home')
    return render(request, "show_lists.html", context)

@login_required(login_url="/login")
def add_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
        return redirect('/home')
    return redirect('/home')

@login_required(login_url="/login")
def show_lists(request):
    pass

@login_required(login_url="/login")
def update_task(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST,instance=task)
        if form.is_valid:
            form.save()
            return redirect('/home')

@login_required(login_url="/login")
def delete_task(request, tid):
    task = Task.objects.get(id=tid)
    task.delete()
    return redirect('/home')

@login_required(login_url="/login")
def delete_list(request, lid):
    todo_list = ToDoList.objects.get(id=lid)
    todo_list.delete()
    return redirect('/home')

def test(request):
    return render(request, "test.html")

