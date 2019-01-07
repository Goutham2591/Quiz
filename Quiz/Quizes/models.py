from django.db import models
from django.utils import timezone
# Create your models here.


class Quiz(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questions = models.CharField(max_length=255)

    def __str__(self):
        return self.questions


class Solution(models.Model):
    Answer = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Points = models.FloatField()

    def __str__(self):
        return self.Answer
