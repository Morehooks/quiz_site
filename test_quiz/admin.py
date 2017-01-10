from django.contrib import admin
from .models import Section, Question, Response


class ResponseInline(admin.StackedInline):
    model = Response
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text', 'section']}),
    ]
    inlines = [ResponseInline]


admin.site.register(Section)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
