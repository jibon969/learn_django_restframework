from django.urls import path, include

urlpatterns = [
    path('', include('watchlist_app.api.urls')),
]