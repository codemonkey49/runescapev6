from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
#https://www.tutorialspoint.com/highcharts/highcharts_configuration_syntax.htm
#https://stackoverflow.com/questions/10563047/accessing-a-python-dictionary-in-javascript
from app.models import *
# Create your views here.
def index(request):
    template="app/index.html"
    context={}
    itemID=440
    data=itemDataPoint.objects.filter(itemID=itemID).order_by("date")
    context["data"]=data
    context["title"]="moose on the loose"
    context["itemID"]=itemID
    
    dataPoints=[]
    dates=[]
    
    #for i in data:
    #    dataPoints.append(i.price)
    #    dates.append(str(i.date))
    #context["dataPoints"]=dataPoints
    context["dates"]=["it","worked"]
    

    return render(request,template,context)
    