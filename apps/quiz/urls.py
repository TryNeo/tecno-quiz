from django.urls import path,register_converter
from .views import *

from ids_encoder import converters


register_converter(converters.HashidsConverter, 'hashids')

urlpatterns = [
     path('', CourseView.as_view(), name='index'),
     path('questions/<hashids:pk>', QuestionView.as_view(), name='question'),
]