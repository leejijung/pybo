from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # 계정이 삭제되면 계정 게시물 모두 삭제
    subject = models.CharField(max_length=200)                  # 질문의 제목
    content = models.TextField()                                # 질문의 내용  
    create_date = models.DateTimeField()                        # 질문을 작성한 일시
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_question')                        # 추천인 추가

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 질문(어떤 질문의 답변인지 알아야하므로 질문 속성이 필요하다)
    content = models.TextField()                                        # 답변의 내용
    create_date = models.DateTimeField()                                # 답변을 작성한 일시
    modify_date = models.DateTimeField(null=True, blank=True)           # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)                                  # 글쓴이
    content = models.TextField()                                                                # 댓글 내용
    create_date = models.DateTimeField()                                                        # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)                                   # 댓글 수정 일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)     # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)         # 이 댓글이 달린 답변