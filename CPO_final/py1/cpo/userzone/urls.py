from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.userzone,name='userzone'),
    url(r'^discussion',views.discussion,name='discussion'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^searchsolution',views.searchsolution,name='searchsolution'),
    url(r'^complainlog',views.complainlog,name='complainlog'),
    url(r'^Logout',views.Logout,name='Logout'),
    url(r'^savecomplain',views.savecomplain,name='savecomplain'),
    url(r'^changepwd',views.changepwd,name='changepwd'),
    url(r'^postquestion',views.postquestion,name='postquestion'),
    url(r'^answer/(?P<qid>\d+)$',views.answer,name='answer'),
    url(r'^postanswer',views.postanswer,name='postanswer'),
    url(r'^viewanswer/(?P<qid>\d+)$',views.viewanswer,name='viewanswer'),
    url(r'^search',views.search,name='search'),

]