from django.shortcuts import render
from . import models
import json

def home(request):
    return render(request,'index.html') 

def group(request):
    return render(request, 'group.html')

def emin(request, id):
    questions = models.Question.objects.filter(compatition_id=id)
    result = dict()
    for question in questions:
        result[f'{question.question_num}'] = models.Result.objects.filter(question_id__question_num=question.question_num)

    
    print(result.keys())
    print(result.values())
    for res in result.keys():
        print(res)
        if res == '1':
            print(result.get(res))
        
    context = {
        'competition_id': id,
        'questions': questions,
        'result': result
    }    
    return render(request, 'emin.html', context)


def competitions(request):
    context = {
        'competitions': models.Compatition.objects.all()
    }

    return render(request, 'competitions.html', context)