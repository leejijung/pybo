from django.contrib.auth import authenticate, login # django.contrib.auth 모듈의 함수로 사용자 인증과 로그인을 담당
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":    # POST요청인 경우 화면에서 입력한 데이터로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # form.cleaned_data.get 함수는 입력값을 개별적으로 얻고싶은 경우에 사용
            user = authenticate(username=username, password = raw_password) # 사용자 인증
            login(request, user)    # 로그인
            return redirect('index')
    else:                       # GET요청인 경우에는 계정생성 화면을 리턴
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
