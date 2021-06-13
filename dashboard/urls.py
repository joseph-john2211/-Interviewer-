from django.urls import path

from . import views

urlpatterns = [
    path('user',views.user, name='user'),
    path('signout',views.signout, name='signout'),
    path('createInterview',views.createInterview,name='createInterview'),
    path('addcandidates',views.addcandidates,name='addcandidates'),
    path('results',views.results,name='results')    
]