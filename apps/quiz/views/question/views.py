from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
import random
from apps.quiz.modelos.model_question import *

class QuestionView(ListView):
    model = Question
    context_object_name  = 'questions'
    template_name = 'Question/question.html'

    def get(self, request,slug,pk, *args, **kwargs):
        name_slug = slug.replace('-', " ").upper()
        data  = {
            'id_question' : [i.toJSON() for i in Question.objects.filter(id_theme__id_course=pk)] 
        }
        dataFin = []
        if len(data['id_question']) !=0:
            for i in range(len(data['id_question'])):
                dataFin.append({
                    'id_question':data['id_question'][i]['id_question'],
                    'question_name':data['id_question'][i]['question_name'],
                    'answers':[],
                    'correct': [x.toJSON() for x in QuestionItem.objects.filter(id_question =data['id_question'][i]['id_question'],correct=True)][0]['name']
                    })
            for i in range(len(dataFin)):
                for x in QuestionItem.objects.filter(id_question =dataFin[i]['id_question']):
                    dataFin[i]['answers'].append({'id_question_item':x.toJSON()['id_question_item'],'name':x.toJSON()['name']})
            dataFin = random.sample(dataFin,20)
        response = JsonResponse(dataFin,safe=False)
        response.status_code = 200
        return render(request,self.template_name,{'data':dataFin,'name_slug':name_slug})