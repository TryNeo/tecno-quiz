from django.db import models
from django.forms import model_to_dict

from apps.quiz.modelos.model_course import *


class Theme(models.Model):
    id_theme = models.AutoField(primary_key=True)
    id_course = models.ForeignKey(Course, verbose_name="Asignatura", on_delete=models.CASCADE)
    name_theme = models.CharField("Tema", max_length=80)

    class Meta:
        db_table = 'quiz_theme'
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'


    def toJSON(self):
        theme_data = model_to_dict(self)
        return theme_data

    def __str__(self):
        return '{}'.format(self.name_theme)