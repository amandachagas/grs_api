from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    movie_id = models.PositiveIntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=300) 
    genres = models.CharField(max_length=300)
    year = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=50, blank=True, default='None')
    imdb_link = models.CharField(max_length=200, blank=True, default='None')
    poster = models.CharField(max_length=500, blank=True, default='None')
    youtubeId = models.CharField(max_length=50, blank=True, default='None')
    tags = models.TextField(max_length=2000, blank=True, default='None')
    counter = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        ordering = ['-counter', 'movie_id']


    def __str__(self):
        return str(self.movie_id)



class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        ordering = ['user_id']
        unique_together = ('user_id', 'movie_id',)