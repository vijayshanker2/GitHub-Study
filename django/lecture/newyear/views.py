from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    status = False
    if day == '25' and month == '12':
        status = True
    return render(request,"newyear/index.html",{
    'status':status
    })
