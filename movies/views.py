from rest_framework.response import Response
from .serializers import MovieSerializer, RatingsSerializer
from .models import Movie, Ratings
from django.db.models import Avg
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class AllMovieViewSet(viewsets.ViewSet):
    serializer_class = MovieSerializer

    def list(self, request):
        movies = Movie.objects.all()
        movie_data = []
        for movie in movies:
            movie_data.append({
                'id': movie.id,
                'name': movie.name,
                'genre': movie.genre,
                'rating': movie.rating,
                'release_date': movie.release_date})

        return Response(movie_data)


class SearchMovieViewSet(viewsets.ViewSet):
    serializer_class = MovieSerializer

    def list(self, request):
        query = request.query_params.get('query', None)
        if query:
            # If a query is provided, search for a single movie
            movie = Movie.objects.filter(name__icontains=query).first()
            if movie:
                # If the movie is found, calculate its average rating
                average_rating = Ratings.objects.filter(
                    movie=movie).aggregate(Avg('rating'))['rating__avg']
                # Serialize the movie data along with the average rating
                movie_data = {
                    'id': movie.id,
                    'name': movie.name,
                    'genre': movie.genre,
                    'rating': movie.rating,
                    'release_date': movie.release_date,
                    'average_rating': average_rating
                }
                return Response(movie_data)
            else:
                # If no movie is found, return a 404 Not Found response
                return Response({'detail': 'Movie not found'}, status=404)
        else:
            # If no query parameter is provided, return a 400 Bad Request response
            return Response({'detail': 'Query parameter "query" is required'}, status=400)
