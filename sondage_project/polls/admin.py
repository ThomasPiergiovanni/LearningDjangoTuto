from django.contrib import admin

# Register your models here.
from .models import Choice, Question


### v3
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

### v4
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    ### v1
    # fields = ['pub_date', 'question_text']

    ### v2
    # fieldsets = [
    #     (None,      {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    ### v3
    # fieldsets = [
    #     (None,      {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    
    ### v5
    # fieldsets = [
    #     (None,      {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text','pub_date', 'was_published_recently')

    ### v6
    # fieldsets = [
    #     (None,      {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text','pub_date', 'was_published_recently')
    # list_filter = ['pub_date']

    ### v7
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

### v2
# admin.site.register(Choice)