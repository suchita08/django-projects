from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^login',views.login,name='login'),
    url(r'^tracking',views.tracking,name='tracking'),
    url(r'^complain',views.complain,name='complain'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^career',views.career,name='career'),
    url(r'^saveenquiry',views.saveenquiry,name='saveenquiry'),
    url(r'^savecomplain',views.savecomplain,name='savecomplain'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
    url(r'^search',views.search,name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)