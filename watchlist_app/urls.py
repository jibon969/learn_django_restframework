from django.urls import path, include

urlpatterns = [
    path('watch/', include('watchlist_app.api.urls')),
]