from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    objects = models.Manager()
    questions = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.questions


