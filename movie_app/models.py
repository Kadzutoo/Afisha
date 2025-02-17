from django.db import models
from django.core.exceptions import ValidationError

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    stars = models.IntegerField(default=1)

    def clean(self):
        if self.stars < 1 or self.stars > 5:
            raise ValidationError({'stars': "Оценка должна быть от 1 до 5."})

    def __str__(self):
        return f'{self.text[:20]}... ({self.stars}⭐)'
