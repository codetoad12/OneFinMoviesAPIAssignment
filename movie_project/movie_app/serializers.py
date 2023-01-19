from rest_framework import serializers
from .models import Collection,Movie,User,GenreRank

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['username','password']

class MovieSerializer(serializers.ModelSerializer):
    uuid=serializers.ReadOnlyField()
   
    class Meta:
        model=Movie
        fields=['uuid','title','description','genres']

 
class CreateCollectionSerializer(serializers.ModelSerializer):

    uuid=serializers.ReadOnlyField()
    movies=MovieSerializer(many=True)
    class Meta:
        model=Collection
        fields=['uuid','title','description','movies']

    def create(self, validated_data):
        movies_data=validated_data.pop('movies')

        user=self.context['user']
        model_user=User.objects.get(username=user)
        collection = Collection.objects.create(user=model_user,**validated_data)
        for data in movies_data:
            Movie.objects.create(collection=collection,user=model_user,**data)
        
        return collection
    
    def update(self, instance, validated_data):
        
        movies_data=validated_data.pop('movies')
        instance.title=validated_data.get('title',instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        for movie_data in movies_data:
            
            movie = Movie.objects.filter(collection=instance,uuid=movie_data.get('uuid')).first()
            if movie:
                movie.title = movie_data.get('title', movie.title)
                movie.description = movie_data.get('description', movie.description)
                movie.genres = movie_data.get('genres', movie.genres)
                movie.user   = self.context['user']
                movie.save()
            else:
                Movie.objects.create(collection=instance,user=self.context['user'],**movie_data)
        
        return instance

class GenreRankSerializer(serializers.ModelSerializer):
    class Meta:
        model=GenreRank
        fields=['genre']

class GetCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Collection
        fields=['uuid','title','description']

  
