from django.db import models
from django.forms import model_to_dict

TEXT_DEFAULT = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Iusto, earum possimus.
Nisi numquam quibusdam deserunt nam sequi mollitia cumque quisquam possimus illum?Expedita."""

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name_course = models.CharField("Asignatura", max_length=60,unique=True)
    description = models.TextField("Descripcion de la Asignatura",default=TEXT_DEFAULT,blank=True,null=True)

    class Meta:
        db_table = 'quiz_course'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'


    def toJSON(self):
        course_data = model_to_dict(self)
        return course_data

    def __str__(self):
        return '{}'.format(self.name_course)
