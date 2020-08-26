from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from my_grs.models import Movie, Rating
from rest_framework import viewsets
from rest_framework import permissions
from my_grs.serializers import UserSerializer, MovieSerializer, RatingSerializer
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import csv


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):

    if request.user.is_authenticated:

        counter = User.objects.count()

        user = User.objects.get(id=int(request.user.id))
        # print(' > > > > > > > {} < < < < < < < <'.format(request.user.id))
        # print(' > > > > > > > {} < < < < < < < <'.format(user))

        if request.method == 'GET':

            try:

                movies_rated = Rating.objects.filter(user_id=user).values('movie_id')
                movies = Movie.objects.exclude(movie_id__in=movies_rated)

            except Movie.DoesNotExist:
                movies = None

            # print(' # # #  {}  # # #'.format(movies[0:10]))

            serializer = MovieSerializer(movies[0:15], many=True)
            
            return render(request, 'home.html', {
                'data': serializer.data,
                'counter': counter
                })

        elif request.method == 'POST':

            movie = Movie.objects.get(movie_id=int(request.POST['this-movie']))

            try:
                rating = Rating.objects.get(user_id=user, movie_id=movie)
                rating.rating = float(request.POST['this-rating'])
                rating.save()
            except:
                Rating.objects.create(
                    user_id=user,
                    movie_id=movie,
                    rating= float(request.POST['this-rating'])
                )

            # print('$ $ $ $ $ {} $ $ $ $ $'.format(request.POST))
            
            return JsonResponse({'success': True})


    else:
        return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
        })


def to_csv(request):

    if request.method == 'POST':
        ratings = Rating.objects.all()

        f = open('./datasets/output.csv', 'w')
        writer = csv.writer(f)
        writer.writerow([
            "userId",
            "movieId",
            "rating"
        ])

        for obj in ratings:
            # print('> | | | | | | > > {}'.format(obj));
            writer.writerow([
                obj.user_id.id,
                obj.movie_id.movie_id,
                obj.rating
            ])

    return JsonResponse({'success': True})