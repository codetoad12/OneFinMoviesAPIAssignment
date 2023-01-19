from django.utils.deprecation import MiddlewareMixin
from django.db.models import Count
#from request_counter.models import RequestCounter
from django.apps import apps
class RequestCounterMiddleware(MiddlewareMixin):
    request_counter=0

    def process_request(self,request,**args):
        self.request_counter+=1
        RequestCounter = apps.get_model('request_counter', 'RequestCount')
        counter=RequestCounter()
        counter.count=self.request_counter
        counter.save()
        sum=RequestCounter.objects.aggregate(Count('count'))
        print(sum['count__count'])
        request.request_count=sum
    