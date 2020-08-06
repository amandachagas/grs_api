from rest_framework import serializers
from my_grs.models import Movie, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['url', 'movie_id', 'title', 'genres', 'year', 'imdb_id', 'imdb_link', 'poster', 'youtubeId', 'tags']



class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['url', 'id', 'user_id', 'movie_id', 'rating']