from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^enquiries',views.enquiries,name='enquiries'),
    url(r'^complains',views.complains,name='complains'),
    url(r'^consignment',views.consignment,name='consignment'),
    url(r'^jobseekers',views.jobseekers,name='jobseekers'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^ addnotification',views.addnotification,name='addnotification'),
    url(r'^deletenotification/(?P<id>\d+)$',views.deletenotification,name='deletenotification'),
    url(r'^deleteenquiries/(?P<id>\d+)$', views.deleteenquiries, name='deleteenquiries'),
    url(r'^deletecomplains/(?P<id>\d+)$', views.deletecomplains, name='deletecomplains'),
    url(r'saveconsignment',views.saveconsignment,name='saveconsignment'),
    url(r'^deletejobseekers/(?P<emailaddress>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deletejobseekers,name='deletejobseekers'),



]