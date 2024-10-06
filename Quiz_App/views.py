from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Question


def quiz_question(request, qid):
    error = ""
    question = get_object_or_404(Question, pk=qid)
    if request.method == 'POST':
        # Get the submitted answer from the form
        submitted_answer = request.POST.get('answer')
        # Assuming your Question model has a field named 'correct_answer'
        # Retrieve the correct answer from the database
        correct_answer = question.correct_answer
        # Compare the submitted answer with the correct answer
        if submitted_answer == correct_answer:
            error = 'no'
        else:
            error='yes'
    return render(request, 'question.html', {'question': question, 'error':error})

def home(request):
    question = Question.objects.all()
    return render(request, 'home.html', {'question': question})

def thanks(request):
    return render(request, 'thanks.html')
