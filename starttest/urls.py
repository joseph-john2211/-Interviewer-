from django.urls import path

from . import views

urlpatterns = [
    path('',views.testregister, name='testregister'),
    path('questionone',views.questionone,name='questionone'),
    path('questiontwo',views.questiontwo,name='questiontwo'),
    path('questionthree',views.questionthree,name='questionthree'),
    path('questionfour',views.questionfour,name='questionfour'),
    path('questionfive',views.questionfive,name='questionfive'),
    path('questionsix',views.questionsix,name='questionsix'),
    path('questionseven',views.questionseven,name='questionseven'),
    path('questioneight',views.questioneight,name='questioneight'),
    path('questionnine',views.questionnine,name='questionnine'),
    path('questionten',views.questionten,name='questionten'),
    path('testcomplete',views.testcomplete,name='testcomplete')

]