from django.db import models


class Section(models.Model):
    section_text = models.CharField(max_length=255)

    def __str__(self):
        return self.section_text


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.response_text


