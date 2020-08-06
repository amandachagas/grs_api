from django.contrib import admin
from my_grs.models import Movie, Rating

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)