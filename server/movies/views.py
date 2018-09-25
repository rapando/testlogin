from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Genre, Movie, Comment
from .serializers import UserSerializer, GenreSerializer, MovieSerializer, CommentSerializer


class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class GenreListCreate(generics.ListCreateAPIView):
    """ List and create genres """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )


class GenreRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update Genre information """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieListCreate(generics.ListCreateAPIView):
    """List and create movies """
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )
