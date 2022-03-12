from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from movie.api.serializers import WatchListModelSerializer, StreamPlatFormModelSerializer
from movie.models import WatchList, StreamPlatForm


@api_view(['GET', 'POST'])
def watch_list(request):
    if request.method == "GET":
        movies = WatchList.objects.all()
        serializer = WatchListModelSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WatchListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# Using class based view
class WatchListAv(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListModelSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def watch_list_details(request, pk):
    if request.method == "GET":
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Movie not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer = WatchListModelSerializer(movie)
        return Response(serializer.data)

    if request.method == "PUT":
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    if request.method == "DELETE":
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListDetailAv(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Movie not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer = WatchListModelSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def stream_plat_form_list(request):
    if request.method == "GET":
        movies = StreamPlatForm.objects.all()
        serializer = StreamPlatFormModelSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WatchListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def stream_plat_form_details(request, pk):
    if request.method == "GET":
        try:
            movie = StreamPlatForm.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Movie not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer = StreamPlatFormModelSerializer(movie)
        return Response(serializer.data)

    if request.method == "PUT":
        movie = StreamPlatForm.objects.get(pk=pk)
        serializer = StreamPlatFormModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    if request.method == "DELETE":
        movie = StreamPlatForm.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Using class based view
class StreamPlatFormAv(APIView):
    def get(self, request):
        movies = StreamPlatForm.objects.all()
        serializer = StreamPlatFormModelSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatFormModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatFormDetailAv(APIView):
    def get(self, request, pk):
        try:
            movie = StreamPlatForm.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Movie not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer = StreamPlatFormModelSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = StreamPlatForm.objects.get(pk=pk)
        serializer = StreamPlatFormModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        movie = StreamPlatForm.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)