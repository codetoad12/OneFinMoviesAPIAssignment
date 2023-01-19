from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import Collection,Movie,GenreRank
from .serializers import CreateCollectionSerializer,GetCollectionSerializer,GenreRankSerializer
from rest_framework.permissions import IsAuthenticated

class CollectionViewset(ModelViewSet):
    queryset=Collection.objects.all()
    serializer_class=CreateCollectionSerializer
    permission_classes=[IsAuthenticated]
    
    def get_serializer_class(self, *args, **kwargs):
        print(self.request.user)
        if(self.request.method=='POST'or self.action=='retrieve'):
            return CreateCollectionSerializer
        
        if (self.action=='list'):
            print(self.action)
            return GetCollectionSerializer
        return CreateCollectionSerializer
    
    def get_serializer_context(self):
        return({"user":self.request.user})

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        collection=Collection.objects.filter(pk=serializer.data['uuid'])
        print(serializer.data['uuid'])
        return Response({"collection_uuid":serializer.data['uuid']},status=HTTP_201_CREATED)
        # Create your views here.
    
    def get_favourite_genres(self):
        ranked_genres=GenreRank.objects.filter(user=self.request.user).order_by('-count')
        count=0
        favourite_genres=[]
        for entry in ranked_genres:
            favourite_genres.append(entry.genre)
            print(entry.count)
            count+=1
            if(count==3):
                break
        return favourite_genres

    def list(self, request, *args, **kwargs):
        
        collection=Collection.objects.filter(user=self.request.user)
        
        collection_serializer=GetCollectionSerializer(collection,many=True)
        collection_list=list(collection_serializer.data)
        print(collection_serializer.data)
        favourite_genres=self.get_favourite_genres()
        print(favourite_genres)
        context={"is_success":True,"data":{"collection":collection_list,'favourite_genres':favourite_genres}}
        return Response(context)
        
    