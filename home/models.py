from django.db import models
from django.template.defaultfilters import truncatewords

# Create your models here.

class Subject(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_question_count(self):
        return Question.objects.filter(topic__subject=self).count()



class Topic(models.Model):
    name=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='topics')

    def __str__(self):
        return self.name


class Question(models.Model):
    question=models.TextField(max_length=2000)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return truncatewords(self.question,10)

class Answer(models.Model):
    answer=models.TextField(max_length=2000)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')

    def __str__(self):
        return truncatewords(self.answer,10)



