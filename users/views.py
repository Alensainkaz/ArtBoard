from django.shortcuts import render,redirect
from .models import User
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login,logout

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request,'users/login.html',context)
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.role='user'
            user.save()
            login(request,user)
            return redirect('index')

    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,'users/register.html',context)
def logout_view(request):
    logout(request)
    return redirect('index')

# Create your views here.
