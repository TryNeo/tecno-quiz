from apps.quiz.views.contact.views import ContactView
from django.urls import path,register_converter

from .views.course.views import *
from .views.question.views import *
from .views.contact.views import *
from .views.onehundredquestion.views import *


from ids_encoder import converters


register_converter(converters.HashidsConverter, 'hashids')

urlpatterns = [
     path('', HomeView.as_view(), name='index'),
     path('course/<str:slug>/questions/<hashids:pk>', QuestionView.as_view(), name='question'),
     path('generate-100-questions/', OnehundredQuestionView.as_view(), name='100-question'),
     path('contact/', ContactView.as_view(), name='contact'),
]