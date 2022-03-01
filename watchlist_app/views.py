from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie


def movie_list(request):
    movie = Movie.objects.all()
    data = {
        'movies': list(movie.values())
    }
    return JsonResponse(data)

