import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    #incase further modification of the user module is required, required variables can be added here

class Movie(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    title=models.CharField(max_length=256)
    description=models.TextField()
    genres=models.TextField()
    collection = models.ForeignKey('Collection', related_name='movies',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class GenreRank(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    genre=models.TextField()
    count=models.IntegerField()

class Collection(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=256)
    description=models.TextField()
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return(self.title)
