from django import forms
from .models import Subject,Topic,Question,Answer
from django.forms import Textarea
class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name']

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['name']

class QuestionForm(forms.ModelForm):
    answer=forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5,'placeholder':'Answer'}

        ),
        max_length=5000,
        help_text='Maximum 5000 words'
    )
    class Meta:
        model=Question
        fields=['question','answer']
        widgets = {
            'question': Textarea(attrs={'rows': 5,'placeholder':'Question'}),
        }

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question']

class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer']

