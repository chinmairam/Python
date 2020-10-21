from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    ordering = ('question_text', '-pub_date')  # In reverse order of pub_date
    search_fields = ('question_text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')
    list_filter = ('choice_text',)
    ordering = ('votes',)
    search_fields = ('choice_text',)
