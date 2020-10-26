from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from login.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):

    return render(request,'login/index.html')


def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            return redirect('inicio')

    return render(request,'users/register.html',{
        'register_form': register_form
    })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('inicio')
    return render(request,'users/login.html')