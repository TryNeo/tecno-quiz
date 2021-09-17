from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView


from apps.quiz.modelos.model_course import *
from apps.quiz.modelos.model_theme import *
from apps.quiz.modelos.model_question import *


class HomeView(ListView):
    model = Course
    context_object_name  = 'courses'
    template_name = 'Home/index.html'

    def get(self, request, *args, **kwargs):
        data  = {
            'id_course' : [i.toJSON() for i in Course.objects.all()] 
        }
        dataFin = []
        for i in range(len(data['id_course'])):
            data['id_course'][i].update({'total_question':Question.objects.filter(id_theme__id_course =data['id_course'][i]['id_course']).count()})
            dataFin.append(data['id_course'][i])
        response = JsonResponse(dataFin,safe=False)
        response.status_code = 200
        return render(request,self.template_name,{'courses':dataFin,"questions_total":Question.objects.all().count()})


    

