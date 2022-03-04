
from django.http.response import JsonResponse
from django.views.generic import ListView

from apps.quiz.modelos.model_course import *
from apps.quiz.modelos.model_question import *

import random




class OnehundredQuestionView(ListView):
    model = Question
    context_object_name  = 'questions'
    template_name = 'onehundredquestion/100-question.html'


    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            
            filter_data = request.POST['courses'].split(",")
            lista = []
            for i in filter_data:
                for x in Question.objects.filter(id_theme__id_course__name_course=i):
                    lista.append(x.toJSON())
            data['id_question'] = lista
            dataFin = []
            if len(data['id_question']) > 100:
                if len(data['id_question']) !=0:
                        for i in range(len(data['id_question'])):
                            image = ''
                            if(data['id_question'][i]['image'] != None):
                                image = data['id_question'][i]['image']
                            dataFin.append({
                                'id_question':data['id_question'][i]['id_question'],
                                'question_name':data['id_question'][i]['question_name'],
                                'image_url': image,
                                'answers':[],
                                'correct': [x.toJSON() for x in QuestionItem.objects.filter(id_question =data['id_question'][i]['id_question'],correct=True)][0]['name']
                                })
                        for i in range(len(dataFin)):
                            for x in QuestionItem.objects.filter(id_question =dataFin[i]['id_question']):
                                dataFin[i]['answers'].append({'id_question_item':x.toJSON()['id_question_item'],'name':x.toJSON()['name']})
                dataFin = random.sample(dataFin,100)
                
                response = JsonResponse(dataFin,safe=False)
                response.status_code = 200
            else:
                response = JsonResponse(dataFin,safe=False)
                response.status_code = 400
        return response



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all() 
        context["total_questions"] = Question.objects.all().count()
        return context
    