from django.shortcuts import render,HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .forms import SubjectForm,TopicForm,QuestionForm,QuestionUpdateForm,AnswerUpdateForm
from .models import Subject,Question,Answer,Topic
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.


@method_decorator(login_required,name='dispatch')
class CreateSubjectView(CreateView):
    form_class = SubjectForm
    template_name = 'create_subject.html '
    success_url = reverse_lazy('subject_list')



class SubjectListView(ListView):
    model=Subject
    context_object_name = 'subjects'
    template_name = 'subject_list.html'
    paginate_by = 10

@method_decorator(login_required,name='dispatch')
class TopicCreateView(CreateView):
    form_class = TopicForm
    template_name = 'create_topic.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['subject_pk']=self.kwargs['pk']

        return context

    def form_valid(self, form):
        subject=get_object_or_404(Subject,pk=self.kwargs['pk'])
        topic=form.save(commit=False)
        topic.subject=subject
        topic.save()
        return redirect('topic_list',pk=subject.pk)


class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['subject']=self.subject
        return context

    def get_queryset(self):
        self.subject=get_object_or_404(Subject,pk=self.kwargs.get('pk'))
        queryset=self.subject.topics.all()
        return queryset


@method_decorator(login_required,name='dispatch')
class QuestionCreateView(CreateView):
    form_class = QuestionForm
    template_name = 'question_create.html'



    def form_valid(self, form):
        self.topic=get_object_or_404(Topic,pk=self.kwargs['topic_pk'],subject__pk=self.kwargs['pk'])
        question=form.save(commit=False)
        question.topic=self.topic
        question.save()
        answer=Answer.objects.create(
            answer=form.cleaned_data.get('answer'),
            question=question
        )
        return redirect('question_list',pk=self.topic.subject.pk,topic_pk=self.topic.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['topic_pk']=self.kwargs['topic_pk']
        return context

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['topic']=self.topic
        return context

    def get_queryset(self):
        self.topic=get_object_or_404(Topic,pk=self.kwargs.get('topic_pk'),subject__pk=self.kwargs.get('pk'))
        queryset=self.topic.questions.all()
        return queryset



@method_decorator(login_required,name='dispatch')
class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionUpdateForm
    context_object_name = 'question'
    pk_url_kwarg = 'question_pk'
    template_name = 'edit_question.html'

    def get_success_url(self):
        return reverse_lazy('question_list',kwargs={'pk':self.kwargs['pk'],'topic_pk':self.kwargs['topic_pk']})

@method_decorator(login_required,name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question
    pk_url_kwarg = 'question_pk'
    template_name = 'question_confirm_delete.html'
    context_object_name = 'question'

    def get_success_url(self):
        return reverse_lazy('question_list',kwargs={'pk':self.kwargs['pk'],'topic_pk':self.kwargs['topic_pk']})

class AnswerListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answer.html'


    def get_queryset(self):
        self.question=get_object_or_404(Question,pk=self.kwargs['question_pk'],topic__pk=self.kwargs['topic_pk'])
        queryset=self.question.answers.all()
        return queryset


@method_decorator(login_required,name='dispatch')
class AnswerUpdateView(UpdateView):
    model = Answer
    form_class = AnswerUpdateForm
    context_object_name = 'answer'
    template_name = 'update_answer.html'
    pk_url_kwarg = 'answer_pk'

    def get_success_url(self):
        return reverse_lazy('question_list',kwargs={'pk':self.kwargs['pk'],'topic_pk':self.kwargs['topic_pk']})




