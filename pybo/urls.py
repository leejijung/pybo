from django.urls import path

from . import views
from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo'

urlpatterns = [ 
    # base_views.py
    path('', base_views.index, name='index'),                                                                                        # 질문 목록
    path('<int:question_id>/', base_views.detail, name='detail'),                                                                    # 선택된 질문
    
    # question_views.py
    
    path('question/create/', question_views.question_create, name='question_create'),                                                    # 질문 작성
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),                                  # 질문 수정
        path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),                                  # 질문 삭제
    
    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),                                        # 답변 작성
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),                                          # 답변 수정
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),                                          # 답변 삭제
    
    # comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),          # 질문 댓글 등록
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),           # 질문 댓글 수정
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),           # 질문 댓글 삭제
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),                  # 답변 댓글 등록
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),                 # 답변 댓글 수정
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),                 # 답변 댓글 삭제

    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),                                           # 질문 추천
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),                                                   # 답변 추천
]