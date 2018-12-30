from django.contrib import admin
from .models import Quiz, Question, Solution
# Register your models here.

class QuizList(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)

admin.site.register(Quiz,QuizList)


class QuestionList(admin.ModelAdmin):
    list_display = ('quiz', 'questions',)
    search_fields = ('quiz', 'questions',)

admin.site.register(Question,QuestionList)

class SolutionList(admin.ModelAdmin):
    list_display = ('Answer','question','Points',)

admin.site.register(Solution,SolutionList)