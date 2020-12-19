from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account for ' + user + ' succesfully created !')
                return redirect('/login')
        context = {"form": form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username)
            print(password)
            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('/home')
            else: 
                messages.warning(request, "Username or password is wrong.")
        return render(request, 'login.html')

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('/home')
