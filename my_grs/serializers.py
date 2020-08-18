from rest_framework import serializers
from my_grs.models import Movie, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title', 'genres', 'year', 'imdb_id', 'imdb_link', 'poster', 'youtubeId', 'tags']



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user_id', 'movie_id', 'rating']