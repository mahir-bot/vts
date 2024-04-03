from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)


class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
