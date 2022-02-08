from http import server
from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #검색 기능 추가
    
admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin) 
# Register your models here.
