from django.contrib import admin
from .models import *

class QuestionItemInline(admin.TabularInline):
    model = QuestionItem


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (QuestionItemInline,)
    list_display = ['question_name',]
    search_fields = ['name','id_question__question_name',]

admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Question,QuestionAdmin)
admin.site.register(QuestionItem)
