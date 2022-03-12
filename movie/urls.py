from django.urls import path, include

urlpatterns = [
    path('watch/', include('movie.api.urls')),
]
