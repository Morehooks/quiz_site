from django.forms import TextInput, Textarea
from django.contrib import admin
from .models import Section, Page, SubPage, Question, Response


class ResponseInline(admin.StackedInline):
    model = Response
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class SubPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['sub_page_header', 'sub_page_seq', 'page']}),
    ]
    inlines = [QuestionInline, ResponseInline]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text', 'question_seq', 'question_type', 'sub_page']}),
    ]
    inlines = [ResponseInline]


admin.site.register(Section)
admin.site.register(Page)
admin.site.register(SubPage, SubPageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
