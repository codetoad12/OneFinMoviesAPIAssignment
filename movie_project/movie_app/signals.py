from .models import GenreRank,Movie
from django.db.models.signals import post_save
from django.dispatch import receiver
from collections import Counter

@receiver(post_save,sender=Movie)
def update_or_create_genre_rank(sender,**kwargs):
    if(kwargs['created']):
        print(kwargs['instance'])
        model_instance=kwargs['instance']
        #print("This",model_instance)
        request_user=model_instance.user
        #print(request_user)
        try:
            GenreRank.objects.filter(user=request_user).delete()
        except:
            print(f"No elements to delete for {request_user}")
        
        movies=Movie.objects.filter(user=request_user)
        
        genres=[]
        for movie in movies:
            genre=movie.genres
            if(','in genre):
                genres.append(genre)
            else:
                genre=genre.split(",")
                for i in genre:
                    i=i.lower()
                    genres.append(i)
            
        genre_count=Counter(genres)
        common_genres=genre_count.most_common(3)
        #print(genre_count)  
        print("This is",common_genres)
        for key in common_genres:
            genre=key[0]
            count=key[-1]
            rank_model=GenreRank.objects.update_or_create(user=request_user,genre=genre,count=count,
                                                          defaults={'user':request_user,'genre':genre})
    

        