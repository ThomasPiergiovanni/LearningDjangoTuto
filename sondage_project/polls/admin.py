from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):

    ### v1
    # fields = ['pub_date', 'question_text']

    ### v2
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)