from django.shortcuts import render
from django.contrib.auth.models import User
from my_grs.models import Movie, Rating
from rest_framework import viewsets
from rest_framework import permissions
from my_grs.serializers import UserSerializer, MovieSerializer, RatingSerializer

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


# @csrf_exempt
# def users_list(request):
#     """
#     List all users, or create a new one.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)