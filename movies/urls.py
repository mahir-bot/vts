from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RatingsViewSet, SearchMovieViewSet, AllMovieViewSet
movie_router = DefaultRouter()
movie_router.register(r'movies', MovieViewSet)
movie_router.register(r'ratings', RatingsViewSet)
movie_router.register(r'all-movie', AllMovieViewSet, basename='all-movie')
movie_router.register(r'search', SearchMovieViewSet, basename='search')

urlpatterns = [
    
]


urlpatterns += movie_router.urls
