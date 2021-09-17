from django.urls import path,register_converter

from .views.course.views import *
from .views.question.views import *

from ids_encoder import converters


register_converter(converters.HashidsConverter, 'hashids')

urlpatterns = [
     path('', HomeView.as_view(), name='index'),
     path('course/<str:slug>/questions/<hashids:pk>', QuestionView.as_view(), name='question'),
]