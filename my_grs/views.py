from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from my_grs.models import Movie, Rating
from rest_framework import viewsets
from rest_framework import permissions
from my_grs.serializers import UserSerializer, MovieSerializer, RatingSerializer
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import csv, json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

                ratings = Rating.objects.filter(user_id=user).values('movie_id')
                movies_rated = Movie.objects.filter(movie_id__in=ratings)

                rated_counter = movies_rated.count()

                # print('>< >< >< >< {}'.format(movies_rated))

                my_dict = []
                for movie in movies_rated:
                    aux = dict()

                    rating = Rating.objects.get(user_id=user, movie_id=movie)

                    # for rating in ratings:
                    #     if movie.movie_id == rating.movie_id.id:
                    aux['title'] = movie.title
                    aux['movie_id'] = movie.movie_id
                    aux['genres'] = movie.genres
                    aux['year'] = movie.year
                    aux['imdb_id'] = movie.imdb_id
                    aux['youtubeId'] = movie.youtubeId
                    aux['poster'] = movie.poster
                    aux['rating'] = float(rating.rating)
                    my_dict.append(aux)

                # print('$ $ $ $ $ $ $ $ {}'.format(my_dict))
                page = request.GET.get('page', 1)

                paginator = Paginator(my_dict, 30)
                
                try:
                    my_dict_pag = paginator.page(page)
                except PageNotAnInteger:
                    my_dict_pag = paginator.page(1)
                except EmptyPage:
                    my_dict_pag = paginator.page(paginator.num_pages)

            except Movie.DoesNotExist:
                my_dict_pag = None

            # print(' # # #  {}  # # #'.format(movies_pag[0:10]))
            
            return render(request, 'home.html', {
                'data': my_dict_pag,
                'counter': counter,
                'rated_counter': 20-rated_counter
                })
    else:
        return render(request, 'home.html')


def evaluate(request):

    if request.user.is_authenticated:

        user = User.objects.get(id=int(request.user.id))
        # print(' > > > > > > > {} < < < < < < < <'.format(request.user.id))
        # print(' > > > > > > > {} < < < < < < < <'.format(user))

        if request.method == 'GET':

            try:

                movies_rated = Rating.objects.filter(user_id=user).values('movie_id')
                movies = Movie.objects.exclude(movie_id__in=movies_rated)

                movies = movies[0:100]

                page = request.GET.get('page', 1)

                paginator = Paginator(movies, 30)
                
                try:
                    movies_pag = paginator.page(page)
                except PageNotAnInteger:
                    movies_pag = paginator.page(1)
                except EmptyPage:
                    movies_pag = paginator.page(paginator.num_pages)

                # print('> > > > > > > > {}'.format(movies_pag))

            except Movie.DoesNotExist:
                movies_pag = None

            # print(' # # #  {}  # # #'.format(movies_pag[0:10]))
            
            return render(request, 'evaluate.html', {
                'data': movies_pag
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
        return render(request, 'evaluate.html')


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

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="output.csv"'

        writer = csv.writer(response)

        # f = open('./datasets/output.csv', 'w')
        # writer = csv.writer(f)
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

        return response

    else:
        return render(request, 'to_csv.html')