from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')       # 로그아웃 상태일 시 로그인 화면으로 이동
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method =="POST":
        form = QuestionForm(request.POST)   # request.POST에는 화면에서 사용자가 입력한 내용들이 담겨있다
        if form.is_valid(): #form이 유효한지 검사
            question = form.save(commit=False) # (commit=False)는 임시저장을 의미
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()   # GET 방식
    
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)  #{'form': form}은 템플릿에서 질문 등록시 사용할 폼 엘리먼트를 생성할 때 쓰인다

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:             # 작성자와 유저가 동일하지 않다면
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')             # 작성자와 유저가 동일하지 않다면 
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')