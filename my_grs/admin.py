from django.contrib import admin
from my_grs.models import Movie, Rating

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    
    list_display = (
        'movie_id',
        'title',
        'genres',
        'tags',
        'imdb_id',
        'imdb_link',
        'youtubeId',
        'poster'

    )


class RatingAdmin(admin.ModelAdmin):
    
    list_display = (
        'user_id',
        'movie_id',
        'rating'
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)