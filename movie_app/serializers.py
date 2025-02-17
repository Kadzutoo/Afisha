from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя режиссера не может быть пустым.")
        return value

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название фильма не может быть пустым.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Длительность фильма должна быть больше 0 минут.")
        return value

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'rating')

class ReviewSerializer(serializers.ModelSerializer):
    stars = serializers.IntegerField(min_value=1, max_value=5)  # Добавляем ограничение на уровне поля

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст отзыва не может быть пустым.")
        return value

    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')
