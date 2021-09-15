from django.db import models
from django.forms import model_to_dict

TEXT_DEFAULT = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Iusto, earum possimus.
Nisi numquam quibusdam deserunt nam sequi mollitia cumque quisquam possimus illum? 
Expedita."""

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name = models.CharField("Asignatura", max_length=50)
    description = models.TextField(default=TEXT_DEFAULT)

    def toJSON(self):
        course_data = model_to_dict(self)
        return course_data

    def __str__(self):
        return '{}'.format(self.name)

class Theme(models.Model):
    id_theme = models.AutoField(primary_key=True)
    id_course = models.ForeignKey(Course, verbose_name="Asignatura", on_delete=models.CASCADE)
    name = models.CharField("Tema", max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question_name = models.CharField("Pregunta", max_length=250)
    id_course = models.ForeignKey(Course, related_name='Asignatura', on_delete=models.CASCADE)
    

    def toJSON(self):
        question_data = model_to_dict(self)
        return question_data

    def __str__(self):
        return '{}'.format(self.question_name)

class QuestionItem(models.Model):
    id_question_item = models.AutoField(primary_key=True)
    name = models.CharField("Texto",max_length=50)
    id_question = models.ForeignKey(Question, related_name='Pregunta', on_delete=models.CASCADE)
    correct = models.BooleanField("Correcta",default=False,blank=True,null=True)

    def toJSON(self):
        question_item_data = model_to_dict(self)
        return question_item_data

    def __str__(self):
        return '{}'.format(self.name)



class QuestionAnswered(models.Model):
    id_question_answered = models.AutoField(primary_key=True)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_question_item = models.ForeignKey(QuestionItem, related_name='Repuesta', on_delete=models.CASCADE)
    correct = models.BooleanField("Correcta",default=False,blank=True,null=True)
    score = models.IntegerField("Puntaje",default=0)
