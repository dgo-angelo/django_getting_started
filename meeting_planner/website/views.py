from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from meetings.models import  Meeting
def welcome(request):
    return render(request,"website/welcome.html",{"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was server at " + str(datetime.now()))

def about(request):
    return HttpResponse("I am Diego de Angelo and I work as a Developer at TOTVS IP")