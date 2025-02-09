from django.urls import path
from .views import (
    DirectorListView, DirectorDetailView,
    MovieListView, MovieDetailView,
    ReviewListView, ReviewDetailView,
    MoviesWithReviewsView, DirectorsWithMoviesCountView
)

urlpatterns = [
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Новые маршруты
    path('movies/reviews/', MoviesWithReviewsView.as_view(), name='movies-with-reviews'),
    path('directors/movies_count/', DirectorsWithMoviesCountView.as_view(), name='directors-with-movies-count'),
]
