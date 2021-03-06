from django.contrib import admin
from my_grs.models import Movie, Rating
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    
    list_display = (
        'movie_id',
        'title',
        'genres',
        'tags',
        'counter',
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


UserAdmin.list_display = ('username', 'id', 'is_staff')
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)