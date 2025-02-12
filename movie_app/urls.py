from django.urls import path
from .views import (
    DirectorCreateView,
    DirectorDetailView,
    DirectorUpdateDeleteView,
    MovieCreateView,
    MovieDetailView,
    MovieUpdateDeleteView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewUpdateDeleteView,
)

urlpatterns = [
    # Режиссеры
    path('directors/', DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('directors/<int:pk>/update-delete/', DirectorUpdateDeleteView.as_view(), name='director-update-delete'),

    # Фильмы
    path('movies/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update-delete/', MovieUpdateDeleteView.as_view(), name='movie-update-delete'),

    # Отзывы
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update-delete/', ReviewUpdateDeleteView.as_view(), name='review-update-delete'),
]