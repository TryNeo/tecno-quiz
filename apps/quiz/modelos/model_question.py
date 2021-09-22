from django.db import models
from django.db.models.fields import URLField
from django.forms import model_to_dict

from apps.quiz.modelos.model_theme import *


class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question_name = models.CharField("Pregunta", max_length=250)
    image = models.URLField("Imagen",max_length = 200,blank=True,null=True)
    id_theme = models.ForeignKey(Theme, related_name='Tema', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'quiz_question'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def toJSON(self):
        question_data = model_to_dict(self)
        return question_data

    def __str__(self):
        return '{}'.format(self.question_name)


class QuestionItem(models.Model):
    id_question_item = models.AutoField(primary_key=True)
    name = models.CharField("Respuesta",max_length=120)
    id_question = models.ForeignKey(Question, related_name='Pregunta', on_delete=models.CASCADE)
    correct = models.BooleanField("Correcta",default=False,blank=True,null=True)

    class Meta:
        db_table = 'quiz_question_item'
        verbose_name = 'Question Item'
        verbose_name_plural = 'Question Items'


    def toJSON(self):
        question_item_data = model_to_dict(self)
        return question_item_data

    def __str__(self):
        return '{}'.format(self.name)