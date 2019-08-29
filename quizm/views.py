from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Question
from .forms import StartForm



def start(request):
    return render(request,'start.html')

def start_quiz(request):
    form = StartForm(request.POST)
    if form.is_valid():
        uid= form.cleaned_data['name']
        request.session["user"] =uid
        request.session['ans'] = ""
        request.session['exclude_id'] = ""
        request.session['score'] = 0
        return redirect("questions")
    return render(request, "start.html", {'form': form})

def question_view(request):
    # import ipdb; ipdb.set_trace()
    answer = request.POST.get('ans')
    if answer:
        request.session['ans'] = f"{request.session['ans']},{answer}"
    exclude_ids = request.session['exclude_id'].split(",")
    exclude_ids = [int(x) for x in exclude_ids if x]
    questions = Question.objects.exclude(id__in=exclude_ids)
    if questions.exists():
        question = questions.first()
        request.session['exclude_id'] = f"{request.session['exclude_id']},{question.id}"
        return render(request, "startq.html", {'question':question})
    return redirect('answers')


def submit_quiz(request):
    data = request.session.get('ans')
    # import ipdb; ipdb.set_trace()
    if data:
        data = data.split(',')
        data = [x for x in data if x]
    questions_id = request.session['exclude_id'].split(',')
    questions_id = [int(x) for x in questions_id if x]
    score = 0
    for i, ques in enumerate(questions_id):
        result = Question.objects.filter(id=ques,answer=data[i])
        if result.exists():
            score = str(int(score)+1)
    return render(request,'answer.html',{'score':score})
        


def logout(request):
   try:
      del request.session['name']
      request.session.flush()
   except:
      pass
   return render(request, "logout.html")




   







