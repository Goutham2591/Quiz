from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    return render(request, 'Quizes/Home.html',
                  {'home': home})


def quiz(request,question_id):
    return render(request, 'Quizes/Quiz.html',
                  {'quiz':quiz})

