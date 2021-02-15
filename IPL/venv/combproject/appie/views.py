from django.shortcuts import render,redirect,reverse
from .match import Match
from .models import event,schedule

# Create your views here.


def seeschedule(request):
    return render(request, 'schedule.html')

def createschedule(request):
    ddmmyy=request.GET['yymmdd']
    yy=int(ddmmyy[:4])
    mm=int(ddmmyy[5:7])
    dd=int(ddmmyy[8:])
    Match(yy,mm,dd)
    sc=schedule.objects.all()
    return render(request, 'scheduled.html',{'sc':sc})