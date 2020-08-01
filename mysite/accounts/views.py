from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def accounts(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('signin') #회원가입 버튼 눌렀을 때, home.html로 이동 
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error':'로그인에 실패하셨습니다. 아이디와 비밀번호를 확인해주세요.'})
            
    return render(request, 'accounts/signin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signin.html')