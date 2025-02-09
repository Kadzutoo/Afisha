from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'rating')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')
