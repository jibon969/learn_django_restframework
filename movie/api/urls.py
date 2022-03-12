from django.urls import path
from movie.api.views import (
    watch_list,
    watch_list_details,
    WatchListAv,
    WatchListDetailAv,
    stream_plat_form_list,
    stream_plat_form_details,
    StreamPlatFormAv,
    StreamPlatFormDetailAv
)

urlpatterns = [
    path('list/', watch_list, name="movie-list"),
    path('<int:pk>/', watch_list_details, name="watch-details"),

    # Api view
    path('watch/', WatchListAv.as_view(), name="watch-list"),
    path('<int:pk>/', WatchListDetailAv.as_view(), name="watch-detail"),

    
    path('stream/', stream_plat_form_list, name="stream-list"),
    path('<int:pk>/', stream_plat_form_details, name="stream-details"),

    # Api view
    path('stream/', StreamPlatFormAv.as_view(), name="stream-list"),
    path('<int:pk>/', StreamPlatFormDetailAv.as_view(), name="stream-detail"),


]