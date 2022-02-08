
from django import forms
from pybo.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] #QuestionForm에서 사용할 Question모델의 속성
        
        """
        # 부트스크랩 클래스 추가
        widgets = {
            'subject' : forms.TextInput(attrs={'class' : 'forms-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }
        """

        # 폼 레이블
        labels ={
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }