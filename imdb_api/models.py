from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length =50)
    about = models.CharField(max_length=255)
    website= models.URLField(max_length= 255)

    def  __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=255)
    platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE, related_name = "watchlist")
    active = models.BooleanField(default =True)
    created = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    review_user = models.ForeignKey(User, on_delete = models.CASCADE)
    desc = models.CharField(max_length= 255)
    watchlist = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = 'Review')
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    


class UNWatchList(models.Model):
    title = models.CharField(max_length= 255)
    storyline= models.CharField(max_length= 250)
    # platform = models.ForeignKey(WatchList, on_delete = models.CASCADE)
    active = models.BooleanField(default= False)
    created = models.DateTimeField()