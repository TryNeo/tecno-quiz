from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class CourseView(ListView):
    model = Course
    context_object_name  = 'courses'
    template_name = 'course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions_total"] = Question.objects.all().count()
        return context
    

class QuestionView(ListView):
    model = Question
    context_object_name  = 'questions'
    template_name = 'question.html'

    def get(self, request,pk, *args, **kwargs):
        data  = {
            'id_question' : [i.toJSON() for i in Question.objects.filter(id_course=pk)] 
        }
        dataFin = []
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
        response = JsonResponse(dataFin,safe=False)
        response.status_code = 200
        return render(request,self.template_name,{'data':dataFin})