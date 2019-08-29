from django.contrib import admin
from quizm.models import Question




   


@admin.register(Question)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('questions', 'choice_one', 'choice_two','choice_three','choice_four','answer')
      


  