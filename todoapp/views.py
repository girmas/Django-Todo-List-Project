from django.shortcuts import render ,redirect
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm,PasswordChangeForm
from todoapp.forms import TodoForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'todoapp/home.html')



def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'todoapp/register.html',{'form':form})




def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('todo')
    else:
        form = AuthenticationForm()
                
        
    return render(request,'todoapp/login.html',{'form':form})

def todotask(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('todo')
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    return render(request,'todoapp/todo.html',{'todo':todo,'form':form})


def logout_user(request):
    auth.logout(request)
    return redirect('login')

def delete_task(request,pk):
    task = Todo.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo')
    return render(request,'todoapp/delete.html',{'task':task})
    
def update_task(request,pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
           form.save()
           return redirect('todo')
    return render(request,'todoapp/update.html',{'task':task,'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Your Password changed successfully")
            return redirect('login')
        else :
            messages.error(request,"something went wrong")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'todoapp/changepassword.html',{'form':form})
    
    