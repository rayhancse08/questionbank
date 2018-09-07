from django.urls import path,include
from home import views

urlpatterns=[
   path('',views.SubjectListView.as_view(),name='subject_list'),
   path('accounts/',include('django.contrib.auth.urls')),
   path('create/',views.CreateSubjectView.as_view(),name='create_subject'),
   path('<int:pk>/',views.TopicListView.as_view(),name='topic_list'),
   path('<int:pk>/create_topic/',views.TopicCreateView.as_view(),name='create_topic'),
   path('<int:pk>/topic/<int:topic_pk>/',views.QuestionListView.as_view(),name='question_list'),
   path('<int:pk>/topic/<int:topic_pk>/create_question/',views.QuestionCreateView.as_view(),name='create_question'),
   path('<int:pk>/topic/<int:topic_pk>/question/<int:question_pk>/edit',views.QuestionUpdateView.as_view(),name='question_edit'),
   path('<int:pk>/topic/<int:topic_pk>/question/<int:question_pk>/delete',views.QuestionDeleteView.as_view(),name='question_delete'),
   path('<int:pk>/topic/<int:topic_pk>/question/<int:question_pk>/answer/',views.AnswerListView.as_view(),name='answer_list'),
   path('<int:pk>/topic/<int:topic_pk>/question/<int:question_pk>/answer/<int:answer_pk>/',views.AnswerUpdateView.as_view(),name='answer_update')


]