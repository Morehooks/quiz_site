from django.db import models


class Section(models.Model):
    section_text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ': ' + self.section_text


class Page(models.Model):
    page_header = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.CASCADE)


class SubPage(models.Model):
    sub_page_header = models.TextField()
    page = models.ForeignKey('Page', on_delete=models.CASCADE)


class Question(models.Model):
    question_seq = models.IntegerField(default=100)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255)
    sub_page = models.ForeignKey('SubPage', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    #def default_question_seq_value(self):
       # if
        #return self.objects.all().aggregate(models.Max(self.question_seq)) + 100


class Response(models.Model):
    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.response_text


