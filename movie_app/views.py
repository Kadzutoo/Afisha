from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

# Список режиссёров с количеством фильмов
class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_queryset(self):
        return Director.objects.annotate(movies_count=Count('movie'))

# Один режиссёр
class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# Список фильмов
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Один фильм
class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Список отзывов
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Один отзыв
class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Фильмы с отзывами и средним рейтингом
class MoviesWithReviewsView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.annotate(rating=Avg('review__stars'))

# Режиссёры с количеством фильмов
class DirectorsWithMoviesCountView(generics.ListAPIView):
    serializer_class = DirectorSerializer

    def get_queryset(self):
        return Director.objects.annotate(movies_count=Count('movie'))
