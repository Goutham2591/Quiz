from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Quiz, Question, Solution

# Create your views here.
def home(request):
    return render(request, 'Quizes/Home.html',
                  {'home': home})


def quiz(request):

    question = Question.objects.all()

    answers = Solution.objects.all()

    return render(request, 'Quizes/Quiz.html',
                  {'question':question, 'answers': answers})


def century_answers(request):
    if request.method == 'POST':
        
    return render(request, 'score.html')


