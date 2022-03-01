from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie


def movie_list(request):
    movie = Movie.objects.all()
    data = {
        'movies': list(movie.values())
    }
    return JsonResponse(data)


# Individual Elements
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }

    return JsonResponse(data)

