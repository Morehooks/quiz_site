from django.db import models


class Section(models.Model):
    section_text = models.CharField(max_length=255)


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)


class Response(models.Model):
    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)


