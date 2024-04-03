from django.contrib import admin
from . import models
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'rating', 'release_date')


class RatingsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating')


admin.site.register(models.Ratings, RatingsAdmin)
admin.site.register(models.Movie, MovieAdmin)
