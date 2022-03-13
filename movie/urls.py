from django.urls import path, include

urlpatterns = [
    path('movie/', include('movie.api.urls')),
]
