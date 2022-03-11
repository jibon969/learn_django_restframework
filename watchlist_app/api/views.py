from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.data)


@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)