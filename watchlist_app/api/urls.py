from django.urls import path
from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieListAv, MovieDetailAv

urlpatterns = [
    path('', movie_list, name="movie-list"),
    path('list/', movie_list, name="movie-list"),
    path('<int:pk>/', movie_details, name="movie-details"),

    # Api view
    path('list-class/', MovieListAv.as_view(), name="movie-list"),
    path('detail/<int:pk>/', MovieDetailAv.as_view(), name="movie-detail"),
]