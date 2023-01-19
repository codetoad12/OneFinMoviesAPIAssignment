from django.shortcuts import render,HttpResponse
from . models import RequestCount 
from django.db.models import Count
# Create your views here.

def show_count(request):
        if(request.method=='GET'):
            sum=RequestCount.objects.aggregate(Count('count'))
            request_number=sum['count__count']
            context={'Request Count':request.request_count}
        return HttpResponse(f"requests:{request_number}")

def reset_count(request):
    if(request.method=='GET'):
        counter=RequestCount.objects.all().delete()
        return HttpResponse("Counter has been Reset")