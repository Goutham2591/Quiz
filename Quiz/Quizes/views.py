from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
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
        century_answer = request.POST
        print(century_answer)

    return render(request, 'Quizes/Score.html',
                  {'century_answer': century_answer})
