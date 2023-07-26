from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, User
from django.contrib import messages


def home_page(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {'students': students, 'teachers': teachers}
    return render(request, 'base/Homepage.html', context)


def Login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, "Username not Found")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                login(request, user)
                messages.success(request, f'{request.user} you Logged in successfully')
                return redirect('home')
            except:
                messages.warning(request, 'Seems like your username or password is invalid!')

    return render(request, 'base/Login.html')


def Logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def register_student(request):
    page = 'stude'
    if request.method == 'POST':
        Student.objects.create(
            names=request.POST.get('names'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            age=request.POST.get('age'),
            code=request.POST.get('code')
        )
        return redirect('home')

    return render(request, 'base/register.html', {'page': page})


@login_required(login_url='login')
def register_teacher(request):
    if request.method == 'POST':
        Teacher.objects.create(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            tscno=request.POST.get('tsc'),
        )
        return redirect('home')
    return render(request, 'base/register.html')
